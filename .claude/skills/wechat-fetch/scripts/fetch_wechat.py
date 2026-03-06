#!/usr/bin/env python3
"""
抓取微信公众号文章内容
"""
import sys
import re
import json
import urllib.request
from urllib.parse import urlparse
from datetime import datetime


def format_timestamp(timestamp_str):
    """
    将时间戳转换为可读格式
    
    Args:
        timestamp_str: 时间戳字符串（秒或毫秒）
    
    Returns:
        str: 格式化后的时间字符串，如果转换失败返回原字符串
    """
    try:
        timestamp = int(timestamp_str)
        
        # 判断是秒还是毫秒
        if timestamp > 1000000000000:  # 毫秒级
            dt = datetime.fromtimestamp(timestamp / 1000)
        else:  # 秒级
            dt = datetime.fromtimestamp(timestamp)
        
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except (ValueError, TypeError):
        return timestamp_str


def fetch_wechat_article(url):
    """
    抓取微信公众号文章内容

    Args:
        url: 微信公众号文章链接

    Returns:
        dict: 包含 title, content, author, publish_time 的字典
    """
    try:
        # 设置请求头模拟浏览器
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0'
        }

        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            html = response.read().decode('utf-8', errors='ignore')

        # 提取标题
        title_match = re.search(r'<h1[^>]*class="rich_media_title[^"]*"[^>]*>(.*?)</h1>', html, re.DOTALL)
        title = title_match.group(1).strip() if title_match else ""
        title = re.sub(r'<[^>]+>', '', title)  # 去除 HTML 标签

        # 提取作者
        author_match = re.search(r'<span[^>]*id="profileBt"[^>]*>.*?<a[^>]*>(.*?)</a>', html, re.DOTALL)
        if not author_match:
            author_match = re.search(r'<a[^>]*id="js_name"[^>]*>(.*?)</a>', html, re.DOTALL)
        author = author_match.group(1).strip() if author_match else ""
        author = re.sub(r'<[^>]+>', '', author)

        # 提取发布时间 - 多种规则尝试
        publish_time = ""
        
        # 规则1: <em id="publish_time">
        time_match = re.search(r'<em[^>]*id="publish_time"[^>]*>(.*?)</em>', html)
        if time_match:
            publish_time = time_match.group(1).strip()
        
        # 规则2: JavaScript 变量 ct
        if not publish_time:
            time_match = re.search(r'var\s+ct\s*=\s*["\']([^"\']+)["\']', html)
            if time_match:
                publish_time = time_match.group(1)
        
        # 规则3: meta 标签
        if not publish_time:
            time_match = re.search(r'<meta[^>]*property="article:published_time"[^>]*content="([^"]+)"', html)
            if time_match:
                publish_time = time_match.group(1)
        
        # 规则4: rich_media_meta_text class
        if not publish_time:
            time_match = re.search(r'<span[^>]*class="rich_media_meta_text[^"]*"[^>]*>(\d{4}-\d{2}-\d{2})</span>', html)
            if time_match:
                publish_time = time_match.group(1)

        # 提取正文内容
        content_match = re.search(r'<div[^>]*id="js_content"[^>]*>(.*?)</div>\s*</div>\s*<script', html, re.DOTALL)
        if content_match:
            content_html = content_match.group(1)
            # 去除 HTML 标签，保留文本
            content = re.sub(r'<[^>]+>', '', content_html)
            content = re.sub(r'\n+', '\n', content)  # 合并多余换行
            content = content.strip()
        else:
            content = ""

        # 提取图片
        images = re.findall(r'data-src="(https?://[^"]+\.(?:jpg|jpeg|png|gif|webp))"', html)

        # 格式化时间戳
        if publish_time:
            publish_time = format_timestamp(publish_time)

        return {
            "title": title,
            "author": author,
            "publish_time": publish_time,
            "content": content[:5000],  # 限制内容长度
            "images": images[:5],  # 最多取 5 张图
            "url": url
        }

    except Exception as e:
        return {"error": f"抓取失败: {str(e)}"}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 fetch_wechat.py <微信文章URL>")
        sys.exit(1)

    url = sys.argv[1]
    result = fetch_wechat_article(url)
    print(json.dumps(result, ensure_ascii=False, indent=2))
