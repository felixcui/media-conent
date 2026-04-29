# 2026 年每个 AI Agent 构建者都必须使用的 Memory Stack（译）

**来源**: https://waytoagi.feishu.cn/wiki/BQ7gwoYQsi1tn2khxh6cOUH9nxf

---

## 摘要

AI代理构建者不应自行构建模型，而应构建一个基于Git事件日志和SQLite索引的可移植记忆层，通过MCP协议向所有工具开放，确保会话重置、模型或工具更换后记忆不丢失，并支持类型定义、可索引、可审计、可同步和高安全性。

---

## 正文

原帖链接：https://x.com/Av1dlive/status/2048800691943309698


这里有一个几乎没人会告诉 AI 构建者的真相。
你不需要自己造模型。
## 你真正需要构建的
是一个存在于所有模型之下的 memory layer。
> **TL;DR**：如果你不想通读全文，就把这个链接丢给你的 agent，然后直接问它问题：[github.com/codejunkie99/brain](https://github.com/codejunkie99/brain)
## 核心论点：memory 应该是可移植的
无论是在 Claude Code 里，还是在 Cursor 里，都该使用同一套存储。
一个 index，能够在会话重置、模型下线、工具切换之后依然存活。
一个 protocol，让所有 harness 都能连接到同一个 brain。
Harrison Chase 在 4 月 21 日用三句话精准点出了这一点。
Taranjeet from Mem0 在 4 月 24 日把它说得更锋利了。
**我同意他们两位的观点。我只是把它再往前推了一步。**
记忆不应仅做到开放，也不应只实现可迁移。它还应当具备类型定义、可索引、可审计、可同步与高安全性。智能体不该只依托无法检视的标记文本块和向量数据库运行。
我花了一个多月时间，构建了正好符合这些要求的东西：
- 基于 Git 的事件日志，每条笔记对应一次提交。
- 搭载 BM25 排序与前缀匹配功能、由 SQLite FTS5 构建的索引。
- 一款 MCP 标准输入输出服务器，向所有兼容智能代理开放五项工具能力。
- 面向人工介入场景的命令行工具（CLI）与全屏终端交互界面（TUI）。
**这篇文章会解释我是怎么把它做出来的，以及为什么每一层都存在。**
如果你只想安装它： [github.com/codejunkie99/brain](https://github.com/codejunkie99/brain)。它支持 Claude Code、Cursor、Codex、OpenClaw、Hermes，或者任何能讲 MCP 或 shell 的工具。
如果你想真正理解你装进去的是什么，那就继续往下读。
## 项目整体形态
7 个 Rust crate。5 个 adapter 目录。大约 9000 行代码。143 个 regression test。一个放在 PATH 里的二进制。
```rust
brain/
├── crates/
│   ├── brain-types     — events, payloads, idempotency keys
│   ├── brain-store     — git-backed event log via libgit2
│   ├── brain-index     — SQLite FTS5, BM25, projections
│   ├── brain-app       — orchestration, two-phase write, catch-up
│   ├── brain-mcp       — rmcp stdio server
│   ├── brain-cli       — `brain` binary
│   └── brain-tui       — full-screen ratatui dashboard
└── adapters/
    ├── claude-code     — MCP config + CLAUDE.md addendum
    ├── cursor          — MCP config + .mdc rule
    ├── codex           — MCP TOML + AGENTS.md addendum
    ├── openclaw        — system-prompt file
    └── hermes          — system-prompt addendum

```

这不是我从第一天就设计好的架构，而是不断试错、不断收敛出来的结果。
**真正的关键洞察，也是 Harrison 那条帖子帮我彻底想明白的地方，是分层。**
- Git 是唯一可信数据源。
- SQLite 为临时索引，可按需从 Git 重新构建。
- 编排层部署在两者之上，负责处理两阶段写入操作。
- 适配器作为轻量化衔接层，确保各运行环境均可调用统一的核心服务。
这意味着：
- 明天换 harness，你不会丢任何东西。
- 明天换模型，你不会丢任何东西。
- 就算 index 整个丢失，也能在几秒内从 git 重建回来。
真正不断积累价值的，只有 git log。而它本质上只是一堆纯 JSON 文件组成的目录。
## 为什么 git 是正确的存储层
我试过的其他方案都有致命缺陷：
- **SQLite-only**：很快，但你得自己解决 replication、conflict resolution 和 audit trail。等于你自己糟糕地重造了半个 git。
- **Markdown files**：利于人工阅读，不利于程序解析。解析速度缓慢。更新操作存在竞态问题。缺乏合理的写入操作单元。
- **DuckDB 或 PostgreSQL**：对于单用户内存场景而言完全大材小用，也无法实现多台笔记本之间的数据同步。
- **Git**：每次事件对应一次提交、单个文件。自带审计日志、支持推拉同步、原生合并机制、差异可视化，可依托任意代码托管平台免费备份。
写入的基本单位是 commit，而 commit 本身就是原子性的。每个 event 都拥有永久不变的 OID。
下面是 `brain-store/src/repo.rs` 里一次 append 的实现：
```rust
pub fn append_event(&self, draft: EventDraft) -> Result<EventRef, StoreError> {
    draft.shallow_validate(SCHEMA_VERSION)?;
    let deadline = Instant::now() + Duration::from_secs(2);
    let mut delay = Duration::from_millis(25);
    loop {
        match self.append_event_once(&draft) {
            Ok(er) => return Ok(er),
            Err(StoreError::Git(ref ge))
                if matches!(ge.code(), ErrorCode::Locked | ErrorCode::Modified)
                    && Instant::now() < deadline =>
            {
                std::thread::sleep(delay);
                delay = min(delay * 2, Duration::from_millis(200));
                continue;
            }
            Err(e) => return Err(e),
        }
    }
}
```

结合指数退避机制的重试循环与幂等键的前置校验，能够让该机制在多并发写入场景下稳定运行。如果采用简单粗暴的「直接提交」方案，一旦两个服务节点在同一毫秒内同时写入，就会直接出现运行异常。
## 为什么检索层选择 SQLite FTS5
Git 是可靠的版本控制工具，但它的搜索速度很慢。使用 git log -S "authlib" 指令虽然可以实现检索，但在包含一万条事件的代码仓库中需要耗时数秒，原因是该指令会对每一次提交重新执行差异对比。
为此，我新增了派生索引。brain-index 库会维护一个 SQLite FTS5 全文检索索引，该索引包含三个加权字段：
- **Title**：10 倍权重
- **Body**：基准权重
- **Tags**：5 倍权重
BM25 来负责排序。写入时使用 `INSERT OR REPLACE`。搜索时，在 100000 个 event 的规模下，top-5 的结果可以在 1 毫秒以内返回。
下面是最关键的两张表，定义在 `brain-index/src/schema.rs`：
```rust
CREATE TABLE events (
      event_id               TEXT PRIMARY KEY NOT NULL,
      commit_oid             TEXT NOT NULL,
      event_type             TEXT NOT NULL,
      subject_kind           TEXT NOT NULL,
      subject_id             TEXT,
      chain_id               TEXT,
      parent_event_id        TEXT,
      actor_kind             TEXT NOT NULL,
      actor_id               TEXT NOT NULL,
      actor_harness          TEXT,
      layer                  TEXT NOT NULL,
      authority_source_kind  TEXT NOT NULL,
      authority_score        INTEGER,
      authority_attested_by  TEXT,
      signature_state        TEXT NOT NULL,
      classification         TEXT NOT NULL,
      time_observed          INTEGER NOT NULL,
      time_recorded          INTEGER NOT NULL,
      idempotency_key        TEXT,
      is_redacted            INTEGER NOT NULL DEFAULT 0,
      payload_json           TEXT NOT NULL
  ) STRICT;

  CREATE VIRTUAL TABLE events_fts USING fts5(
      event_id UNINDEXED,
      title,
      body,
      tags,
      tokenize = 'unicode61 remove_diacritics 2',
      prefix   = '2 3 4'
  );

  CREATE TABLE pref_current (
      category   TEXT NOT NULL,
      key        TEXT NOT NULL,
      value_json TEXT NOT NULL,
      event_id   TEXT NOT NULL,
      updated_at INTEGER NOT NULL,
      PRIMARY KEY (category, key)
  ) STRICT;

  CREATE TABLE claim_current (
      schema_type           TEXT NOT NULL,
      key                   TEXT NOT NULL,
      event_id              TEXT NOT NULL,
      chain_id              TEXT NOT NULL,
      content_json          TEXT NOT NULL,
      supersedes_event_id   TEXT,
      verdict               TEXT,
      verdict_event_id      TEXT,
      verdict_at            INTEGER,
      is_archived           INTEGER NOT NULL DEFAULT 0,
      updated_at            INTEGER NOT NULL,
      PRIMARY KEY (schema_type, key)
  ) STRICT;

  CREATE TABLE watermark (
      key   TEXT PRIMARY KEY NOT NULL,
      value TEXT NOT NULL
  ) STRICT;

```

关键细节：该索引为衍生生成。如果索引损坏、版本结构升级，或是被手动刻意删除，执行 brain doctor --deep 命令即可一次性从 Git 中重新构建索引。
Git 历史记录是唯一可信的核心依据，索引仅作为缓存存在。
我最初尝试过嵌入向量方案，但其运行速度更慢、架构更复杂，还需要依赖额外模型。对于事件数量不足十万的单用户系统，基于 FTS5 实现的 BM25 算法，检索效果与之几乎无差别。
最终，简洁的加权公式方案脱颖而出。
## 10 种事件类型
记忆并非单一事物。偏好不等于经验教训，主张不等于客观事实。三者需要不同的检索规则、不同的可见性语义以及不同的更新策略。
```rust
pub enum EventPayload {
    Observe(ObservePayload),      // "I chose X over Y"
    Claim(ClaimPayload),          // "warfarin + ibuprofen is dangerous"
    Lesson(LessonPayload),        // distilled pattern across episodes
    Pref(PrefPayload),            // "I always use tabs"
    SkillEdit(SkillEditPayload),  // "I modified skill X for reason Y"
    Verify(VerifyPayload),        // attestation on a prior claim
    Archive(ArchivePayload),      // hide without deleting
    Redact(RedactPayload),        // scrub and roll back projections
    Import(ImportPayload),        // bulk load from external source
    Audit(AuditPayload),          // system event
}

```

每个变体都拥有独立的负载结构体：
- Claims 带有 `schema_type + key + content + supersedes`，支持 chain-aware retrieval。
- Prefs 带有 `category + key + value`。
- Redacts 带有一个 `reason`，并且会触发 projection rollback。
类型系统本身就是重点。`current_pref("auth", "provider")` 返回的是通过 materialized projection 上的 SQL lookup 得到的当前值，而不是在一团 markdown blob 里做字符串匹配。
**Typed memory 才是可查询的 memory。**
每个 event 还带有完整的 metadata：`event_id`（基于 UUIDv7，可按时间排序）、actor.kind + actor.id + actor.harness、chain_id、time_observed、time_recorded、layer、authority、signature_state、classification、schema_version、idempotency_key。
其中 `actor.harness` 字段，是实现实现跨工具溯源能力的关键。Claude Code 写下的一条 note，从内容上看和 Cursor 写下的一条 note 没有区别。真正告诉你“这条是谁通过哪个工具写出来的”，就是这个 harness 字段。
## Redact 会回滚，而不是抹除
如果你 redact 掉当前 Pref tip，最天真的做法是直接删掉 projection row。但这样做的后果是 `current_pref` 会变空，这意味着用户连更早之前的历史值也一起丢掉了。
正确做法应该是 rollback。Redact Pref B 时，projection 要恢复成它的前驱 Pref A。就像是 memory 版的 `git revert`。
在 `brain-index/src/ingest.rs` 中：
```rust

EventPayload::Redact(r) => {
    let pref_keys: Option<(String, String)> = tx.query_row(
        "SELECT category, key FROM pref_current WHERE event_id = ?1",
        params![target],
        |row| Ok((row.get::<_, String>(0)?, row.get::<_, String>(1)?)),
    ).optional()?;

    tx.execute("DELETE FROM pref_current WHERE event_id = ?1", params![target])?;

    if let Some((cat, key)) = pref_keys {
        let predecessor = tx.query_row(
            r#"SELECT event_id, payload_json, time_recorded
                 FROM events
                WHERE event_type = 'pref'
                  AND is_redacted = 0
                  AND event_id != ?1
                  AND json_extract(payload_json, '$.category') = ?2
                  AND json_extract(payload_json, '$.key')      = ?3
             ORDER BY time_recorded DESC, event_id DESC
                LIMIT 1"#,
            params![target, cat, key], |row| { /* ... */ },
        ).optional()?;
        // restore predecessor into pref_current
    }
}

```

这里的 `ORDER BY time_recorded DESC, event_id DESC` 很关键。因为当多条记录落在同一毫秒时，如果不这么做，predecessor 的选择会变得不确定。UUIDv7 的随机尾部用来打破这种并列。
## 那个隐藏得很深的 prefilter
每个被序列化后的 event，在写进 git 之前，都会先经过一个 `RegexSet` 扫描。
- 18 条 pattern
- 使用 NFKC Unicode normalization，防止 fullwidth lookalike 字符绕过检测
- 去除 zero-width 字符，防止利用 ZWSP 偷渡
在 `brain-store/src/secrets.rs` 中：
```rust
const RAW_PATTERNS: &[(&str, &str)] = &[
    // Anthropic FIRST. The openai-key pattern is a superset of
    // `sk-ant-...` and would otherwise win in RegexSet (lowest index).
    ("anthropic-key",      r"\bsk-ant-[A-Za-z0-9_-]{20,}\b"),
    ("openai-key",         r"\bsk-(?:proj-)?[A-Za-z0-9][A-Za-z0-9_-]{20,}\b"),
    ("github-token",       r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{80,})\b"),
    ("aws-access-key-id",  r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    ("db-uri-credentials", r"\b(?:postgres|mysql|mongodb|redis|amqp)://[^:\s/@]+:[^@\s]{4,}@\S+"),
    ("slack-token",        r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    ("stripe-live-key",    r"\bsk_live_[A-Za-z0-9]{24,}\b"),
    ("google-api-key",     r"\bAIza[0-9A-Za-z_-]{35}\b"),
    ("vault-token",        r"\b(?:hvs|hvb|s)\.[A-Za-z0-9._-]{20,}\b"),
    ("twilio-auth-token",  r"(?i)\btwilio[_-]?auth[_-]?token\b.{0,3}[=:].{0,3}[0-9a-f]{32}\b"),
    ("jwt",                r"\beyJ[A-Za-z0-9_=-]+\.[A-Za-z0-9_=-]+\.[A-Za-z0-9_.+/=-]*\b"),
    ("pem-private-key",    r"-----BEGIN (?:RSA |OPENSSH |DSA |EC )?PRIVATE KEY-----"),
    ("bearer-token",       r"(?i)\bbearer\s+[A-Za-z0-9._~+/-]{20,}\b"),
    // 5 more patterns elided
];

```

扫描过程分为三个阶段执行：
1. 扫描原始输入。
1. 去掉 zero-width 字符再扫描一次，用来拦截类似 `s\u{200B}k-ant-...` 这种伪装。
1. 执行 NFKC 标准化处理（将全角 ASCII 字符与数学字母数字字符统一转换为普通 ASCII 字符），再次剔除零宽字符，随后重新扫描。
```rust
pub fn detect_secret_text(raw: &str) -> Option<&'static str> {
    // Pass 1: raw scan. Catches the common case with no allocation.
    if let Some(idx) = PATTERNS.set.matches(raw).iter().next() {
        return Some(PATTERNS.names[idx]);
    }
    // Pass 2: strip zero-width chars and rescan. Blocks
    // "s\u{200B}k-ant-..." from smuggling through.
    if raw.chars().any(is_zero_width) {
        let normalized: String = raw.chars().filter(|c| !is_zero_width(*c)).collect();
        if let Some(idx) = PATTERNS.set.matches(&normalized).iter().next() {
            return Some(PATTERNS.names[idx]);
        }
    }
    // Pass 3: NFKC normalize (folds fullwidth ASCII + mathematical
    // alphanumerics to plain ASCII) then strip zero-width.
    let nfkc: String = raw.nfkc().filter(|c| !is_zero_width(*c)).collect();
    if nfkc != raw {
        if let Some(idx) = PATTERNS.set.matches(&nfkc).iter().next() {
            return Some(PATTERNS.names[idx]);
        }
    }
    None
}

```

其中 `pem-private-key` 是一个兜底防线。
- 假设一段 GCP service-account blob 被贴进了 `Observe.content`，它会先被 JSON 转义，于是 `"type":"service_account"` 会变成 `\"type\":\"service_account\"`，从而让原本结构化的 `gcp-service-account` pattern 匹配不到。
- 但 `-----BEGIN PRIVATE KEY-----` 这种内容不会受到 JSON 转义影响，因此这个兜底 pattern 仍然能把它抓出来。
这件事我是在 Codex 第 11 轮 审查时才学到的。
commit subject 也会被脱敏处理。对于 `Observe`、`Lesson`、`Redact` 这 3 种自由文本变体场景，subject 会直接用 `event_id`，而不是回显用户文本。
否则，一段漏过 prefilter 的 secret，就会被进一步提升到 `git log --oneline` 的永久历史里。
## 那些我一开始没想到必须要有的 forgery defenses
事实证明，防 commit-level tampering 比我想象中要麻烦。最后我加了 3 个成本很低的防线，它们都在同一个函数 `event_from_commit` 里：
- **Trailer-block parsing**：`event_id:` trailer 只从 commit message 的最后一个段落里解析，也就是最后一个空行之后的部分。这样用户就不能通过在 note 里附一个 `\n\nevent_id: <forged>` 来偷渡 trailer。
- **Blob-trailer cross-check**：blob 内部的 `event_id` 必须同时和 trailer 里的 `event_id` 以及文件名一致。这样可以阻止“trailer 指向错误 blob”这种伪造。
- **Filename-in-parent skip**：每个 git commit 都带着累积的 `events/` tree。一个伪造 commit 如果复用了旧 event 的文件名，会让 `event_count` 膨胀，并污染 `find_by_idempotency_key`。修复方式是：如果某个 `events/<id>.json` 已经存在于任意 parent tree 中，那这个 commit 就不算真正引入了这个 event，直接跳过。
```rust
fn event_from_commit(&self, commit: &git2::Commit<'_>) -> Result<Option<Event>, StoreError> {
    let Some(trailer_event_id) = event_id_from_commit_message(commit.message().unwrap_or("")) else {
        return Ok(None);
    };
    let tree = commit.tree()?;
    let events_entry = match tree.get_name("events") {
        Some(e) if e.kind() == Some(ObjectType::Tree) => e,
        _ => return Ok(None),
    };
    let events_tree = self.repo.find_tree(events_entry.id())?;
    let filename = format!("{}.json", trailer_event_id);
    let file_entry = match events_tree.get_name(&filename) {
        Some(e) => e,
        None => return Ok(None),
    };
    let blob_oid = file_entry.id();

    // Defense #3: filename-in-parent skip.
    for parent in commit.parents() {
        let Ok(parent_tree) = parent.tree() else { continue; };
        let Some(pe) = parent_tree.get_name("events") else { continue; };
        if pe.kind() != Some(ObjectType::Tree) { continue; }
        let Ok(pet) = self.repo.find_tree(pe.id()) else { continue; };
        if pet.get_name(&filename).is_some() {
            return Ok(None);  // inherited from parent, not introduced here
        }
    }

    let blob = self.repo.find_blob(blob_oid)?;
    let mut event: Event = deserialize_event_blob(&blob)?;

    // Defense #2: blob/trailer cross-check.
    if event.event_id != trailer_event_id {
        return Err(StoreError::ForgedCommit {
            oid: commit.id().to_string(),
            detail: format!(
                "trailer claims {} but blob contains {}",
                trailer_event_id, event.event_id
            ),
        });
    }

    event.commit_oid = commit.id().to_string();
    Ok(Some(event))
}

```

伪造行为在实际场景中，仅当他人能够向你的核心目录写入数据时才会产生影响。但该防护方案仅需20行代码即可实现，对应的测试工作也十分简单。
我完成了13轮对抗性代码审查。此类攻击手段反复出现，直至第三道防护机制部署完成后才得以遏制。
实话实说：该防护手段无法阻挡拥有终端访问权限、蓄意发起攻击的入侵者。它主要用于防范意外异常，以及从恶意镜像仓库拉取到的被篡改提交记录，这也正是该威胁模型的设计目标。
## Two-phase write 与 catch-up reconciliation
Git commit 很慢，大约 10ms。SQLite index 写入很快，大约 1ms。简单的单事务处理方式，会让每一次写入操作都被迫采用两者中速度更慢的执行方式。
所以我用了下面这种方式：
1. 先写入 git（source of truth，持久化层）。
1. 再写入 index（best-effort，更快）。
1. 如果进程在两个操作之间异常终止，<code>catch_up_index</code> 会在下次打开时执行数据同步修复。
生产环境里的做法大概长这样：
三条 reconciliation path：
- **Fast path**：watermark 与 HEAD 一致，并且 event count 一样，什么都不做。
- **Orphan path**：index 里有 git 没有的 event。说明历史被重写了，或者导入了外来的 index。直接从 git 全量重建。
- **Replay path**：index 只是 git 的严格子集。那就从第一个缺失 event 开始往后 replay，依靠 ingest 的 idempotency 来保持 projection ordering 正确。
真正花了不少 review 才想透的细节，是“从最早缺失事件开始整体往前 replay”。
那个看起来显然正确的版本，也就是“只 ingest 缺失的事件”，在缺失事件和已索引事件交错出现时会出问题。
它会把当前 tip projection 用过时数据覆盖掉。
只有从最早缺失的事件开始，按顺序整体重放到最新，projection ordering 才能保持单调正确。
## MCP server：tool description 比 implementation 更重要
Brain 暴露了 5 个 MCP 工具。一旦接入，所有兼容的 AI 工具都可以直接使用。
在 `brain-mcp/src/lib.rs` 中：
```rust
#[tool_router(server_handler)]
impl BrainMcp {
    #[tool(description = "Ping the brain server; returns 'pong' if alive.")]
    async fn ping(&self) -> String { "pong".to_string() }

    #[tool(description = "\
Save a persistent note to the user's long-term memory. CALL THIS WHENEVER:
- the user states a preference or convention
- the user shares a decision or rationale you'd want to recall next session
- you finish a non-trivial task and a lesson emerged
- the user asks you to remember something
Do NOT call this for ephemeral context that only matters in the current turn.
Written to a git-backed event log, durable across sessions and tools.")]
    async fn note(&self, args: NoteArgs) -> Result<String, ErrorData> { /* ... */ }

    #[tool(description = "\
Search the user's long-term memory. Returns up to 5 matches.
CALL THIS PROACTIVELY at the start of non-trivial tasks:
- before picking a library, pattern, or config value
- before running a migration, deploy, or schema change
- when the user references prior decisions
- when the user asks 'didn't we fix this before?'
Prefix-matching is automatic — typing `fast` finds `fastapi-users`.")]
    async fn ask(&self, args: AskArgs) -> Result<String, ErrorData> { /* ... */ }

    // log and doctor similarly prescriptive
}

```

Agent 读取的是 description。它会根据 description 来决定自己要不要调用这个工具。
一个写着“当你不确定时就调用我”的 description，会比一个只写“返回 top 5 匹配结果”的 description 被调用得多得多。
每个工具的 description 里，我写的都不只是 **WHAT**，而是 **WHEN**。这才是真正的杠杆点。
## FTS5 query rewriting
FTS5 默认是 exact-token match。如果你输入 `fast`，哪怕明明有很多关于 `fastapi` 的 note，它也可能什么都搜不到。
这是一个致命的 UX bug。
修复代码在 `brain-index/src/query.rs`：
如果一个 query 没有显式 operator，就按 tokenizer boundary 把它拆开，并给每个 token 自动追加 `*`。这样裸词就会自动变成前缀查询。
```rust
fn escape_fts(raw: &str) -> String {
    let has_explicit_operator = raw
        .chars()
        .any(|c| matches!(c, '*' | '"' | '(' | ')' | ':'))
        || raw
            .split_whitespace()
            .any(|w| matches!(w, "AND" | "OR" | "NOT"));
    if has_explicit_operator {
        // Balanced quotes → phrase query, pass through. Odd count →
        // stray quote, double for safety.
        let quote_count = raw.chars().filter(|&c| c == '"').count();
        if quote_count.is_multiple_of(2) {
            return raw.to_string();
        }
        return raw.replace('"', "\"\"");
    }
    // Split on tokenizer boundaries (non-alphanumeric + not `_`) and
    // append `*` to each token. Bare words become prefix queries.
    let mut tokens = Vec::new();
    let mut current = String::new();
    for c in raw.chars() {
        if c.is_alphanumeric() || c == '_' {
            current.push(c);
        } else if !current.is_empty() {
            tokens.push(format!("{current}*"));
            current.clear();
        }
    }
    if !current.is_empty() {
        tokens.push(format!("{current}*"));
    }
    tokens.join(" ")
}

```

这样一来：
- `ask fast` → `fast*` → 能匹配到 `fastapi`
- `ask fastapi-users` → `fastapi* users*` → 两个 token 都能匹配
- `ask cargo build` → `cargo* build*` → 隐式 AND，同时找两个词
- `ask "exact phrase"` → 原样透传
- `ask auth*` → 原样透传，不会变成双星号
FTS5 parse error 在 search path 中会被静默捕获，并返回空结果，而不是冒泡成一个 500。这样就算某个 MCP client 不小心传进来一个 `foo(bar`，也不会把整个 session 直接撞挂。
## 通过 git push / pull 来同步
Brain 本身就是一个 git repo。所以同步，就是 `git push` 和 `git pull`。我只是把它们包装成了 CLI 命令。
直接 shell out 到 git，本身就能白拿 SSH key、HTTPS credential manager、2FA、macOS Keychain，以及企业级 SSO。
不需要额外配置。不需要 daemon。不需要 cloud。所有脏活累活都让 git 来做。
## 跨工具测试
一旦这 5 个 harness 全都指向同一个 `~/.brain`，那么 Claude Code 写下的一条 note，就会对 Cursor、Codex、OpenClaw、Hermes 同时可见。
这是我用来验证安装是否真的成功的测试：
```bash
# In Claude Code:
> use brain.note to save: "we use authlib for PKCE, not fastapi-users"
[brain.note is called]
Saved.

# In Cursor, new session, different project:
> what did we decide about auth?
[Cursor's agent calls brain.ask "auth" via MCP]
Based on brain memory: you chose authlib over fastapi-users for PKCE.

# In Codex CLI:
$ codex "what's our auth stack?"
[Codex calls brain.ask "auth"]
You use authlib for PKCE (not fastapi-users).

```

**三个不同工具。三个不同进程。一个共享 memory。**
这正是我真正想要的东西。
## 这个构建过程里到底发生了什么
**第 1 周。**我先把 core 搭起来：types、store、index。整整两天没有任何东西能编译通过，因为 libgit2 的 `Repository` 是 `!Send`，而我又必须把它穿过 async code。最后的解法是在 orchestration layer 使用 `spawn_blocking`，而不是硬跟 lifetime 对抗。
**第 2 到第 3 周。**我完成了 MCP server。第一版的 tool description 写的是 “Save a note.”。结果 agent 根本不会主动调用它，除非我明确提示。于是我把 description 重写成强制式、指令式的“CALL THIS WHENEVER”风格。然后 agent 开始在没人提醒的情况下主动调用。
> 对 MCP 来说，tool description 的重要性，高于 tool implementation 本身。
也是在第 3 周，我差点直接放弃。`brain ask fast` 明明应该命中 10 条提到 `fastapi` 的 note，但结果什么也没有。我重建了 3 次 index，写了一个 ingest 100 条 event 并断言 retrieval 的测试。测试通过了。CLI 依然什么都搜不到。
后来我更仔细地读了 FTS5 文档。它默认就是 exact-token match。那天晚上我把 query rewriter 写了出来。第二天早上，整个系统的可用性直接提升了 10 倍。
**第 4 到第 5 周。**进入 Codex review 的第 5 到第 11 轮。一共修了 12 个问题，从 secret-prefilter bypass 到 commit-trailer injection，再到 watermark race condition。新增了 30 个 regression test。
整个模式几乎总是一样：Codex 指出一段只有 5 行的代码，我会先想“这没问题吧”，然后我写一个专门试图破坏它的测试，而那个测试通常真的能把它打爆。
**第 6 周。**我给 5 个 harness 全都写好了 adapter。大部分工作其实是 system-prompt template 的编写，以及把每个 harness 的 include 语法调对。光是和 Cursor 的 `.mdc` frontmatter 打架，我就花了半天，因为它的 `alwaysApply` 想稳定工作，就得老老实实用字面量的 `["**/*"]` glob。
**第 7 周。**我写了 `brain push`、`brain pull` 和 `brain remote`。整个过程花了 30 分钟，因为真正干活的是 git。
**第 8 周。**做 TUI 的打磨：按天分组、tool glyph、filter key。起因很简单，我突然意识到我已经从 4 个工具里收集了 200 多条 note，却没有任何方式按工具维度把它们看清楚。
**第 9 周。**我撞上了一堵墙：source-pollution bug。每一条 note 都会匹配每一个 query。`brain ask brain` 会返回所有 note。`brain ask fastapi` 也会返回所有 note。
> 我不想把它夸得太神。这个系统并不魔法，甚至也谈不上特别聪明。它真正做到的，是一致性。
> 它会把每一条 note 都 commit 下来。Index 出错时它会重建 index。它拒绝写入 secret。它不会今天记得、明天就忘记上周学到的东西。
> 这种一致性，在几个月时间里不断累积之后，会带来一种与无状态 agent 明显不同的体验，即便底层模型根本没有变化。
## 使用时要特别注意什么
**Index drift**
- 问题：index 里有 git 没有的 event，或者反过来。搜索会返回 ghosts，或者漏掉真实 note。
- 解决办法：`brain doctor --deep`。它会从 git 一次性重建 index。
**Source-field FTS pollution**
- 问题：某个 metadata field 被错误索引进 body 列，导致每个 query 都匹配每条 note。
- 解决办法：只 allow-list 那些真正应该进入 FTS 的字段。再写一个专门搜“本不该命中任何结果的 token”的测试。
**Detached HEAD writes**
- 问题：一次写入如果落在 detached HEAD 上，下次 branch checkout 就会直接蒸发。
- 解决办法：在 open time 和 append time 都拒绝 detached HEAD。Brain 会直接拒绝写入，直到你重新 attach。
**Concurrent-writer races**
- 问题：两个 agent 恰好同一毫秒 commit，其中一个会输掉 HEAD compare-and-swap。
- 解决办法：exponential backoff retry loop，加上 idempotency-key 的预检查，防止 retry 时双重落地。
**Schema mismatch on upgrade**
- 问题：新版本 brain 提升了 FTS schema，旧的 index 文件已经不兼容。
- 解决办法：rebuild self-heal。open 时检测到 mismatch，删除旧 sqlite 文件，再从 git 重建。
**Secret leaked into commit subject**
- 问题：用户输入的 free-form 文本如果进了 commit subject，就会永久存在于 `git log --oneline` 里。
- 解决办法：对 `Observe`、`Lesson`、`Redact` 做 subject scrubbing。直接用 `event_id`，永远不要回显用户原文。
## 如果重新来一遍，我会做哪些不同的决定
第一天就把 retrieval test 写出来。source-pollution bug 本来可以很早就被发现，只要我一开始就有这样一个测试：“一条完全没提到 brain 的 note，不应该被 `ask brain` 命中。”但我直到第 9 周才写出这个测试。
> 写测试时，要验证用户体验，而不只是单元正确性。
每写 500 行代码就跑一次 adversarial review，而不是每 5000 行才做一次。我把 13 轮 Codex review 全都堆到了后面。如果我在每个 major feature 之后就跑一轮，大多数修复都只会是 5 行，而不是后面那种 50 行级别的重构。
一开始就使用 typed errors。`StoreError::InvalidState { detail: String }` 把 6 种完全不同的情况都塞进了同一个 stringly-typed variant。调用方根本无法分辨哪些是 recoverable，哪些已经接近 corruption。
一开始就把 tool description 写成 prescriptive 风格。那种泛泛而谈的描述，例如 “Save a note”，根本不会被调用。只有那种明确告诉 agent **WHEN** 该调用的描述，才会触发主动使用。这是我做过杠杆最高的一次改动。
在 API 稳定之前，不要急着拆 repo。我曾经试图在代码稳定之前，就把 `brain` 从 `agentic-stack` 的 parent repo 里拆出去。结果来回 re-sync 了 3 次。应该再等等。
## 最终结论
现在，这套系统还只是为一个人、在一组工具之间提供 memory。但工具会来，也会走。模型会被淘汰。Harness 会因为新的 IDE 插件而改变，旧的会逐渐腐烂。你的 skill 会随着项目一起演化。
真正会在多年时间里持续积累价值的，只有 memory：你做过什么决定、试过什么、失败过什么、什么有效、什么是你永远不会再做第二次的。
- 模型，可以在出现更好的东西时随时替换。
- Skills 和 protocols，可以随着工作方式一起重写。
- 但 memory 无法替代。它编码的是你独有的错误、你独有的决策、你独有的工作方式。
把你的 memory 掌握在自己手里。把你的索引掌握在自己手里。把它们保存在 plain file 和 git 里，放在任何公司都拿不走的地方。
## **致谢**
这篇文章的 理论 受到 Harrison Chase（LangChain CEO）的启发，也被 Mem0 的 Taranjeet 进一步 sharpen 了。正是他先说出了 “memory lock-in” 这个词，而那时我还没意识到这正是我需要的 framing。
我在一个下午写出了第一版。但完整 stack 花了三个月。并且从那之后，它几乎每周都在变得更好，甚至很多时候我根本没有再去碰它。
## 声明
*这篇文章由作者本人完成研究与写作，由 Minimax-M2.7 编辑。缩略图取自 Pinterest。*
*Harrison Chase: “memory should be open!” — https://x.com/hwchase17/status/2046308913939919232**Harrison Chase: “Your Harness, Your Memory” — https://www.langchain.com/blog/your-harness-your-memory**Vivek Trivedi: “The Anatomy of an Agent Harness” — https://www.langchain.com/blog/the-anatomy-of-an-agent-harness*