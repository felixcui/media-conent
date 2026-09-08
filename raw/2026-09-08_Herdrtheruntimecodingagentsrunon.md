# Herdr: the runtime coding agents run on

**来源**: https://herdr.dev/

---

## 摘要

Herdr 是一个开源（Apache-2.0）的 AI 编码 Agent 运行时基础设施（YC F26）：以后台服务器持有各 Agent 的真实终端会话，合上笔记本、断网、断 SSH 后工作不中断，重启后可恢复布局与会话；自动检测每个 Agent 的状态（working / blocked / idle）并汇聚成注意力队列，无需逐个终端排查。支持 Claude Code、Codex、Cursor、opencode、Grok、Copilot、Hermes 等 20 种 Agent 开箱即用，提供终端 UI、SSH、手机等多端接入以及 CLI / socket API 供 Agent 互相操控协作。上线四个月获 25k GitHub stars、34 万下载，社区插件超 500 个。

---

## 正文

### 定位：Agent 的"运行时"

Herdr 不是又一个 Agent，也不是 tmux 的简单换皮，而是把"编码 Agent 的宿主环境"做成了基础设施：

- **Always running**：herdr-server 在后台运行，终端会话活在服务里。合盖、断网，Agent 继续干活；重启机器后布局和会话自动恢复
- **注意力队列**：读取每个窗格状态并标记 working / blocked / idle，某个 Agent 停下来等输入时会主动报告，不用逐个 pane 找"卡住的那个"
- **Agent-native**：CLI 和 socket API 是同一套接口，Agent 可以互相分屏、启动对方、发 prompt，并能等待另一个 Agent 真正 blocked 再继续，而不是盲目发按键
- **Runs what you already run**：不包装不替代现有 Agent CLI，只"接管"它们的终端，一个二进制覆盖 macOS / Linux / Windows

### 与 tmux 的关系

HN 上讨论最多的对比：Herdr 被称为"为 agentic workflow 优化的 tmux"——鼠标可点击、状态可视化、选中即复制。有用户评价"用了几天后回不去了"，也有人指出性能和可扩展性不如成熟的 tmux。Herdr 官方博客（Coding agents are becoming runtimes）的立场是：Agent CLI 正在成为开发者基础设施，而运行时层面的契约应该由 Agent 主动暴露生命周期信号；Herdr 目前用"可验证生命周期信号 + 屏幕读取兜底 + 热加载检测清单"做桥接，并将发布按 Agent 的支持矩阵。

### 规模

- 开源协议 Apache-2.0
- 上线 4 个月：25k GitHub stars，340k 下载
- 社区插件市场首月突破 500 个插件
- GitHub: https://github.com/herdrdev/herdr

### 安装

```bash
curl -fsSL https://herdr.dev/install.sh | sh
```
