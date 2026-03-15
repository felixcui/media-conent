#!/usr/bin/env python3
"""
News Collect - 一站式资讯收集工具
功能：抓取文章 → 使用 OpenClaw 大模型生成摘要 → 推送到飞书
"""
import sys
import re
import json
import urllib.request
import urllib.parse
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

# ============ 配置 ============
WEBHOOK_URL = "https://www.feishu.cn/flow/api/trigger-webhook/4ebcdc4fd26c38187fdd74434d17a916"
OPENCLAW_AGENT = "fs_news_claw"  # agent ID


# ============ 内容抓取 ============

def is_wechat_article(url):
    """判断是否是微信公众号文章"""
    return 'mp.weixin.qq.com' in url or 'weixin.qq.com' in url


def format_timestamp(timestamp_str):
    """将时间戳转换为可读格式"""
    try:
        timestamp = int(timestamp_str)
        if timestamp > 1000000000000:  # 毫秒级
            dt = datetime.fromtimestamp(timestamp / 1000)
        else:  # 秒级
            dt = datetime.fromtimestamp(timestamp)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except (ValueError, TypeError):
        return timestamp_str


def fetch_wechat_article(url):
    """抓取微信公众号文章内容"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0'
        }
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=30) as response:
            html = response.read().decode('utf-8', errors='ignore')

        # 提取标题
        title_match = re.search(r'<h1[^>]*class="rich_media_title[^"]*"[^>]*>(.*?)</h1>', html, re.DOTALL)
        title = title_match.group(1).strip() if title_match else ""
        title = re.sub(r'<[^>]+>', '', title)

        # 提取作者
        author_match = re.search(r'<span[^>]*id="profileBt"[^>]*>.*?<a[^>]*>(.*?)</a>', html, re.DOTALL)
        if not author_match:
            author_match = re.search(r'<a[^>]*id="js_name"[^>]*>(.*?)</a>', html, re.DOTALL)
        author = author_match.group(1).strip() if author_match else ""
        author = re.sub(r'<[^>]+>', '', author)

        # 提取发布时间
        publish_time = ""
        time_patterns = [
            r'<em[^>]*id="publish_time"[^>]*>(.*?)</em>',
            r'var\s+ct\s*=\s*["\']([^"\']+)["\']',
            r'<meta[^>]*property="article:published_time"[^>]*content="([^"]+)"',
            r'<span[^>]*class="rich_media_meta_text[^"]*"[^>]*>(\d{4}-\d{2}-\d{2})</span>',
        ]
        for pattern in time_patterns:
            match = re.search(pattern, html)
            if match:
                publish_time = match.group(1).strip()
                break
        publish_time = format_timestamp(publish_time)

        # 提取正文
        content_match = re.search(r'<div[^>]*id="js_content"[^>]*>(.*?)</div>\s*</div>\s*<script', html, re.DOTALL)
        if content_match:
            content = re.sub(r'<[^>]+>', '', content_match.group(1))
            content = re.sub(r'\n+', '\n', content).strip()
        else:
            content = ""

        return {
            "title": title,
            "author": author,
            "publish_time": publish_time,
            "content": content,
            "url": url
        }

    except Exception as e:
        return {"error": f"抓取失败: {str(e)}"}


def fetch_generic_article(url):
    """抓取普通网页内容"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0'
        }
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=30) as response:
            content_type = response.headers.get('Content-Type', '')
            encoding = 'utf-8'
            if 'charset=' in content_type:
                encoding = content_type.split('charset=')[1].split(';')[0].strip()
            html = response.read().decode(encoding, errors='ignore')

        # 提取标题
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
        title = re.sub(r'\s+', ' ', title_match.group(1).strip()) if title_match else ""

        # 提取正文
        content_selectors = [
            r'<article[^>]*>(.*?)</article>',
            r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>',
            r'<div[^>]*class="[^"]*article[^"]*"[^>]*>(.*?)</div>',
            r'<div[^>]*id="content"[^>]*>(.*?)</div>',
            r'<div[^>]*id="article"[^>]*>(.*?)</div>',
        ]
        
        content = ""
        for pattern in content_selectors:
            match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
            if match:
                content = re.sub(r'<[^>]+>', ' ', match.group(1))
                content = re.sub(r'\s+', ' ', content).strip()
                if len(content) > 200:
                    break

        return {
            "title": title,
            "author": "",
            "publish_time": "",
            "content": content,
            "url": url
        }

    except Exception as e:
        return {"error": f"抓取失败: {str(e)}"}


def fetch_article(url):
    """统一抓取文章接口"""
    if is_wechat_article(url):
        return fetch_wechat_article(url)
    return fetch_generic_article(url)


# ============ 摘要生成（使用 OpenClaw agent） ============

def generate_summary_with_llm(content, title="", max_length=200):
    """
    使用 Claude Code 生成文章摘要
    """
    if not content:
        return ""
    
    # 清理内容，限制长度
    content = content.strip()[:3000]
    
    # 构建 prompt
    prompt = f"""请为以下文章生成一个简洁的摘要，要求：
1. 长度控制在 {max_length} 字以内
2. 突出文章的核心观点和关键信息
3. 语言简洁明了，避免冗余
4. 不要包含代码、命令行等技术细节
5. 直接输出摘要内容，不要添加任何说明或标题

文章标题：{title}

文章内容：
{content}
"""

    # 使用 Claude Code 生成摘要
    try:
        print("   使用 Claude Code 生成摘要...")
        result = subprocess.run(
            ["claude", "-p", "--permission-mode", "bypassPermissions", "--output-format", "text", prompt],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            summary = result.stdout.strip()
            # 清理摘要
            summary = re.sub(r'^["\']|["\']$', '', summary)
            summary = re.sub(r'^(摘要|总结)[:：]?\s*', '', summary)
            
            if len(summary) > 50:
                if len(summary) > max_length:
                    summary = summary[:max_length-3] + "..."
                print(f"   使用 Claude Code 生成摘要 ({len(summary)}字)")
                return summary
    except Exception as e:
        print(f"   Claude Code 不可用: {e}")
    
    # Fallback: 使用规则生成摘要
    print("   使用规则生成摘要...")
    return generate_summary_rule_based(content, title, max_length)


def generate_summary_rule_based(content, title="", max_length=200):
    """基于规则生成文章摘要"""
    if not content:
        return ""
    
    content = content.strip()
    
    # 清理内容：去除多余空白、特殊字符
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'[🦞📝🛠️💡🔥⭐✨✅❌📌📎]', '', content)
    
    # 提取句子
    sentences = re.split(r'[。！？\n]', content)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 15]
    
    # 过滤掉代码、命令行、URL
    filtered_sentences = []
    for sent in sentences:
        # 跳过代码片段
        if sent.startswith('```') or sent.startswith('python') or sent.startswith('npm'):
            continue
        if sent.startswith('$') or sent.startswith('>'):
            continue
        # 跳过纯 URL
        if re.match(r'^https?://', sent):
            continue
        # 跳过过短的句子
        if len(sent) < 20:
            continue
        filtered_sentences.append(sent)
    
    # 关键句识别（优先级排序）
    key_patterns = [
        r'(介绍|分享|讲解|说明|阐述).{10,50}(方法|方案|技巧|经验|教程|流程|系统)',
        r'(核心|关键|要点|重点).{10,50}(是|在于|为)',
        r'(总结|结论|建议).{10,50}',
        r'(实现|搭建|构建|创建).{10,50}(自动化|系统|工具|流程)',
        r'(使用|采用|通过).{10,50}(OpenClaw|Claude|AI|工具)',
    ]
    
    key_sentences = []
    normal_sentences = []
    
    for sent in filtered_sentences[:15]:
        is_key = any(re.search(pattern, sent) for pattern in key_patterns)
        if is_key and len(sent) > 20 and len(sent) < 120:
            key_sentences.append(sent)
        elif len(sent) > 20 and len(sent) < 100:
            normal_sentences.append(sent)
    
    # 构建摘要：优先关键句，补充普通句
    summary_parts = []
    
    if key_sentences:
        summary_parts.extend(key_sentences[:2])
    
    if len(''.join(summary_parts)) < 80 and normal_sentences:
        needed = 2 if len(summary_parts) == 0 else 1
        summary_parts.extend(normal_sentences[:needed])
    
    # 合并并清理
    summary = '。'.join(summary_parts)
    summary = re.sub(r'。+', '。', summary)
    summary = summary.strip('。')
    
    # 控制长度
    if len(summary) > max_length:
        # 尝试在句子边界截断
        truncated = summary[:max_length-3]
        last_period = truncated.rfind('。')
        if last_period > max_length * 0.7:
            summary = truncated[:last_period+1]
        else:
            summary = truncated + "..."
    
    return summary


# ============ 飞书推送 ============

def push_to_feishu(url, title, summary, webhook_url=None):
    """推送文章到飞书 webhook"""
    webhook = webhook_url or WEBHOOK_URL
    
    data = {
        "url": url,
        "title": title,
        "summary": summary
    }
    
    try:
        req = urllib.request.Request(
            webhook,
            data=json.dumps(data, ensure_ascii=False).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result.get("code") == 0, result
            
    except Exception as e:
        return False, {"error": str(e)}


# ============ 主流程 ============

def main():
    parser = argparse.ArgumentParser(description='News Collect - 资讯收集工具')
    parser.add_argument('url', help='文章URL')
    parser.add_argument('--webhook', help='自定义飞书webhook地址')
    parser.add_argument('--no-push', action='store_true', help='不推送到飞书，仅输出结果')
    parser.add_argument('--summary-length', type=int, default=200, help='摘要长度（默认200字）')
    
    args = parser.parse_args()
    
    print(f"🚀 开始抓取: {args.url}")
    
    # 1. 抓取内容
    data = fetch_article(args.url)
    
    if "error" in data:
        print(f"❌ 抓取失败: {data['error']}")
        sys.exit(1)
    
    print(f"✅ 抓取成功: {data['title']}")
    if data['author']:
        print(f"   作者: {data['author']}")
    
    # 2. 生成摘要
    print("📝 生成摘要...")
    summary = generate_summary_with_llm(data['content'], data['title'], args.summary_length)
    print(f"✅ 摘要生成完成 ({len(summary)}字)")
    
    # 3. 输出结果
    result = {
        "url": args.url,
        "title": data['title'],
        "author": data['author'],
        "publish_time": data['publish_time'],
        "summary": summary
    }
    
    print("\n" + "="*50)
    print("📋 收集结果:")
    print("="*50)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 4. 推送到飞书
    if not args.no_push:
        print("\n📤 推送到飞书...")
        success, response = push_to_feishu(
            args.url, 
            data['title'], 
            summary, 
            args.webhook
        )
        
        if success:
            print("✅ 推送成功！")
        else:
            print(f"❌ 推送失败: {response}")
            sys.exit(1)
    
    print("\n✨ 完成!")


if __name__ == "__main__":
    main()
