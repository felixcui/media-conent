---
name: news-collect
description: "一站式资讯收集工具：抓取文章 → 使用大模型生成摘要 → 推送到飞书。支持微信公众号文章和普通网页，完全自动化处理。"
metadata: { "openclaw": { "emoji": "📰", "requires": { "bins": ["python3", "openclaw"] } } }
---

# News Collector - 一站式资讯收集工具

一个脚本完成所有操作：抓取文章 → 使用大模型生成摘要 → 推送到飞书多维表格。

## 功能特点

- ✅ **一站式处理**：一个命令完成抓取、摘要、推送全流程
- ✅ **大模型摘要**：使用 OpenClaw 或 Claude Code 生成高质量摘要
- ✅ **支持多源**：微信公众号文章、普通网页自动识别
- ✅ **自动降级**：如果大模型不可用，自动使用规则生成摘要
- ✅ **自动推送**：直接推送到飞书 webhook

## 前置要求

- Python 3.6+
- OpenClaw CLI 或 Claude Code CLI（用于生成摘要）

安装方式（二选一）：
```bash
# 方式1：使用 OpenClaw（推荐）
npm install -g openclaw@latest

# 方式2：使用 Claude Code
npm install -g @anthropic-ai/claude-code
```

## 使用方法

### 基础用法（抓取 + 大模型摘要 + 推送）

```bash
python3 scripts/collect.py <文章URL>
```

示例：
```bash
python3 scripts/collect.py "https://mp.weixin.qq.com/s/nhzMNSc_-TQefSLz9Gb08A"
```

### 仅抓取不推送

```bash
python3 scripts/collect.py <文章URL> --no-push
```

### 自定义 webhook

```bash
python3 scripts/collect.py <文章URL> --webhook "https://your-webhook-url"
```

### 调整摘要长度

```bash
python3 scripts/collect.py <文章URL> --summary-length 150
```

## 输出示例

```
🚀 开始抓取: https://mp.weixin.qq.com/s/...
✅ 抓取成功: 🦞 写作、排版、发布一条龙...
   作者: AI工具进化论
📝 生成摘要（使用大模型）...
✅ 摘要生成完成 (156字)

==================================================
📋 收集结果:
==================================================
{
  "url": "https://mp.weixin.qq.com/s/...",
  "title": "🦞 写作、排版、发布一条龙...",
  "author": "AI工具进化论",
  "publish_time": "2026-03-15 20:33:23",
  "summary": "作者分享了使用OpenClaw+Claude Code+wenyan-cli搭建全自动化公众号写作系统的经验，实现选题、写作、配图、排版、发布全流程自动化。建议主文章人工把控质量，次条三条用自动化，每天30-60分钟即可完成内容生产。"
}

📤 推送到飞书...
✅ 推送成功！

✨ 完成!
```

## 支持的来源

| 来源类型 | 自动识别 | 支持内容 |
|---------|---------|---------|
| 微信公众号 | ✅ | 标题、作者、发布时间、正文 |
| 普通网页 | ✅ | 标题、正文 |

## 配置

默认 webhook 地址（可在脚本中修改）：
```python
WEBHOOK_URL = "https://www.feishu.cn/flow/api/trigger-webhook/4ebcdc4fd26c38187fdd74434d17a916"
```

发送字段：
- `url`: 文章链接
- `title`: 文章标题
- `summary`: 生成的摘要（由大模型生成）

## 参数说明

| 参数 | 说明 | 默认值 |
|-----|------|-------|
| `url` | 文章链接（必填） | - |
| `--webhook` | 自定义飞书 webhook | 内置地址 |
| `--no-push` | 仅抓取，不推送 | False |
| `--summary-length` | 摘要最大长度 | 200 |

## 摘要生成逻辑

1. **优先使用 OpenClaw**：调用 `openclaw run` 命令生成高质量摘要
2. **备选 Claude Code**：如果 OpenClaw 不可用，尝试使用 `claude -p`
3. **自动降级**：如果都不可用，自动使用规则生成摘要
4. **智能清理**：自动去除 emoji、代码片段、URL 等干扰内容
5. **长度控制**：严格控制在指定字数范围内

## 文件结构

```
news_collect/
├── SKILL.md              # 技能文档
└── scripts/
    ├── collect.py        # ⭐ 主脚本（一站式）
    └── fetch_content.py  # 旧版（保留兼容）
```

## 更新日志

### v2.0 (2026-03-15)
- 新增：使用 Claude Code 大模型生成摘要
- 新增：自动降级机制（Claude 失败时使用规则生成）
- 优化：摘要质量大幅提升，更准确地提取核心观点

### v1.0
- 基础功能：抓取、规则摘要、推送
