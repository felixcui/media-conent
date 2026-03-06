---
name: news-collect
description: "Extract news article content, generate AI-powered summary (150-200 words), and push to Feishu Bitable via webhook. Supports WeChat articles (uses wechat-fetch skill) and general web pages. Sends url, title, summary to Feishu webhook. The agent generates the summary using its own LLM capabilities; no external API key required."
metadata: { "openclaw": { "emoji": "📰", "requires": { "bins": ["python3"] } } }
---

# News Collector

Collect news articles, extract content, generate AI-powered summary, and push to Feishu Bitable.

## Workflow

1. **Fetch content** - Run `scripts/fetch_content.py` to extract title and body from article
2. **Generate summary** - Agent creates 150-200 character summary using its LLM
3. **Push to Feishu** - Agent sends url, title, summary via webhook

## Supported Sources

- **WeChat articles** (`mp.weixin.qq.com`) - Automatically uses wechat-fetch skill
- **General web pages** - Generic HTML extraction

## Usage

Step 1: Fetch article content

```bash
python3 scripts/fetch_content.py <article-url>
```

This returns:

```json
{
  "title": "Article Title",
  "content": "Full article content...",
  "author": "...",
  "publish_time": "..."
}
```

Step 2: Generate summary (agent does this)

The agent reads the content and generates a 150-200 character summary capturing key points.

**Summary requirements:**
- Length: 150-200 Chinese characters
- Focus: Core points and key information
- Style: Concise and clear
- Exclude: Code snippets, URLs, UI text

Step 3: Push to Feishu

Agent sends to webhook:

```json
{
  "url": "https://...",
  "title": "Article Title",
  "summary": "Generated summary (150-200 chars)"
}
```

## Webhook

Webhook URL: `https://www.feishu.cn/flow/api/trigger-webhook/4ebcdc4fd26c38187fdd74434d17a916`

Fields sent: `url`, `title`, `summary`

## Example

```bash
# Step 1: Fetch content
python3 scripts/fetch_content.py "https://mp.weixin.qq.com/s/example"

# Agent then generates summary and sends to Feishu automatically
```

