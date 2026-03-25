#!/usr/bin/env python3
"""
AI 资讯获取与分类脚本 V4 最终版
使用智谱 AI 进行智能分类
"""
import requests
import json
import os
from datetime import datetime, timedelta

# 需要过滤的公众号ID列表
EXCLUDED_BIZ_IDS = {
    "3092970861",
    "3975307385",
    "3870521375",
    "3573172279",
    "3087180557",
    "3271657808",
    "2397888542",
    "2390216734"
}

# RSS API 配置
RSS_API_KEY = os.getenv("AI_NEWS_API_KEY", "5O5H1c1NsT")
RSS_API_BASE = os.getenv("AI_NEWS_API_BASE", "https://wexinrss.zeabur.app")

# 智谱 API 配置
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY", "07edc94107ae4f8cb08010eaf2aede1f.Sn7KC0rYwqySG2PK")
ZHIPU_BASE_URL = "https://open.bigmodel.cn/api/paas/v4"


def classify_with_ai(news_list):
    """使用智谱 AI 进行智能分类"""
    
    if not news_list:
        return {}
    
    print(f"🤖 使用智谱 AI 分类 {len(news_list)} 条资讯...")
    
    # 准备资讯标题列表
    news_text = "\\n".join([f"{i+1}. {item['title']}" for i, item in enumerate(news_list)])
    
    prompt = f"""分类：
{news_text}

类别：AI编程、AI模型与技术、AI产品与应用、AI行业动态及观察、其他
JSON格式：{{"类别":[索引]}}"""
    
    try:
        from openai import OpenAI
        
        client = OpenAI(
            api_key=ZHIPU_API_KEY,
            base_url=ZHIPU_BASE_URL
        )
        
        # 重试机制
        import time
        max_retries = 3
        for attempt in range(max_retries):
            try:
                print(f"  尝试 {attempt + 1}/{max_retries}...")
                
                response = client.chat.completions.create(
                    model="glm-5",
                    messages=[
                        {"role": "system", "content": "分类助手，只输出JSON。"},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.1,
                    max_tokens=8000
                )
                
                content = response.choices[0].message.content
                
                # 提取 JSON
                start_idx = content.find('{')
                end_idx = content.rfind('}') + 1
                if start_idx != -1 and end_idx > start_idx:
                    json_text = content[start_idx:end_idx]
                    categories = json.loads(json_text)
                    
                    # 转换分类名称到标准格式
                    mapped_categories = {}
                    cat_mapping = {
                        "AI编程": "AI编程",
                        "AI模型与技术": "AI模型与技术",
                        "AI产品与应用": "AI产品与应用",
                        "AI行业动态及观察": "AI行业动态及观察",
                        "其他": "其他"
                    }
                    
                    for cat_name, indices in categories.items():
                        if cat_name in cat_mapping:
                            mapped_categories[cat_mapping[cat_name]] = indices
                    
                    print(f"✅ 智谱 AI 分类完成")
                    return validate_categories(mapped_categories, len(news_list))
                
                print(f"⚠️ 智谱 API 返回格式不正确，使用关键词分类")
                return classify_by_keywords(news_list)
                
            except Exception as e:
                error_msg = str(e)
                if "429" in error_msg or "rate limit" in error_msg.lower():
                    if attempt < max_retries - 1:
                        wait_time = (attempt + 1) * 2
                        print(f"  ⏳ 请求频率过高，等待 {wait_time} 秒后重试...")
                        time.sleep(wait_time)
                        continue
                    else:
                        print(f"  ⚠️ 重试次数用尽，使用关键词分类")
                        return classify_by_keywords(news_list)
                else:
                    raise
        
        return classify_by_keywords(news_list)
        
    except ImportError:
        print("⚠️ 未安装 openai 库，使用关键词分类")
        return classify_by_keywords(news_list)
    except Exception as e:
        print(f"⚠️ 智谱 AI 分类失败: {str(e)[:100]}，使用关键词分类")
        return classify_by_keywords(news_list)


def validate_categories(categories, total_count):
    """验证分类结果是否有效"""
    if not categories:
        return {}
    
    classified_indices = set()
    for cat_name, indices in categories.items():
        if isinstance(indices, list):
            for idx in indices:
                if isinstance(idx, int) and 1 <= idx <= total_count:
                    classified_indices.add(idx)
    
    if len(classified_indices) == total_count:
        return categories
    
    missing = [i for i in range(1, total_count + 1) if i not in classified_indices]
    if missing:
        if "其他" not in categories:
            categories["其他"] = []
        categories["其他"].extend(missing)
    
    return categories


def classify_by_keywords(news_list):
    """关键词分类后备方案"""
    categories = {
        "AI编程": [],
        "AI模型与技术": [],
        "AI产品与应用": [],
        "AI行业动态及观察": [],
        "其他": [],
    }

    coding_keywords = ["编程", "代码", "开发", "IDE", "Git", "DevOps", "软件工程", "Cursor", "OpenClaw"]
    model_tech_keywords = ["模型", "GPT", "Claude", "大模型", "算法", "训练", "推理", "架构", "论文"]
    product_app_keywords = ["产品", "应用", "Agent", "智能体", "平台", "工具", "Skill", "MCP"]
    industry_keywords = ["融资", "上市", "IPO", "人事", "离职", "入职", "GTC", "演讲", "行业"]

    for i, news in enumerate(news_list):
        title = news["title"]
        classified = False

        for keyword in coding_keywords:
            if keyword in title:
                categories["AI编程"].append(i + 1)
                classified = True
                break

        if not classified:
            for keyword in model_tech_keywords:
                if keyword in title:
                    categories["AI模型与技术"].append(i + 1)
                    classified = True
                    break

        if not classified:
            for keyword in product_app_keywords:
                if keyword in title:
                    categories["AI产品与应用"].append(i + 1)
                    classified = True
                    break

        if not classified:
            for keyword in industry_keywords:
                if keyword in title:
                    categories["AI行业动态及观察"].append(i + 1)
                    classified = True
                    break

        if not classified:
            categories["其他"].append(i + 1)

    return {k: v for k, v in categories.items() if v}


def get_news_summary(days: int = 1) -> str:
    """获取并分类汇总 AI 资讯"""
    
    today = datetime.now()
    yesterday = today - timedelta(days=days)
    after = yesterday.strftime("%Y%m%d")
    before = today.strftime("%Y%m%d")
    url = f"{RSS_API_BASE}/api/query?k={RSS_API_KEY}&content=0&before={before}&after={after}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        news_list = []
        if isinstance(data, dict) and 'data' in data and isinstance(data['data'], list):
            for item in data['data']:
                if isinstance(item, dict):
                    biz_id = str(item.get("biz_id", ""))
                    if biz_id in EXCLUDED_BIZ_IDS:
                        continue

                    title = item.get("title", "")
                    link = item.get("link", "")
                    biz_name = item.get("biz_name", "")
                    
                    if title and link:
                        if len(title) > 200 or title.count('\\n') > 1 or title.count('。') > 3:
                            continue
                        news_list.append({
                            "title": title,
                            "link": link,
                            "biz_name": biz_name
                        })

        if not news_list:
            return f"""## AI 资讯汇总

> 📅 `{yesterday.strftime('%Y-%m-%d')}` - `{today.strftime('%Y-%m-%d')}`

😊 暂无AI相关资讯，请稍后再来查看～
"""

        print(f"📰 获取到 {len(news_list)} 条资讯，开始分类...")
        
        categories = classify_with_ai(news_list)
        
        return format_output(news_list, categories, yesterday, today)

    except Exception as e:
        return f"""## ❌ 获取 AI 资讯失败

> 错误信息：`{str(e)}`

请检查网络连接或 API 配置后重试。
"""


def format_output(news_list, categories, start_date, end_date):
    """格式化输出"""
    lines = []
    lines.append("## AI 资讯汇总")
    lines.append("")
    lines.append(f"> 📅 `{start_date.strftime('%Y-%m-%d')}` - `{end_date.strftime('%Y-%m-%d')}`")
    lines.append("")
    
    ai_news_count = sum(len(indices) for indices in categories.values())
    
    if ai_news_count == 0:
        lines.append("😊 暂无AI相关资讯～")
        lines.append("")
        return "\\n".join(lines)
    
    category_order = [
        "AI编程",
        "AI模型与技术",
        "AI产品与应用",
        "AI行业动态及观察",
        "其他"
    ]
    
    for category in category_order:
        if category not in categories or not categories[category]:
            continue
            
        indices = categories[category]
        lines.append(f"### {category}（{len(indices)} 条）")
        lines.append("")
        
        for i, idx in enumerate(indices, 1):
            if idx < 1 or idx > len(news_list):
                continue
            news = news_list[idx - 1]
            title = news["title"]
            link = news["link"]
            biz_name = news.get("biz_name", "")
            
            if biz_name:
                lines.append(f"{i}. [{title}]({link}) `{biz_name}`")
            else:
                lines.append(f"{i}. [{title}]({link})")
        
        lines.append("")
    
    return "\\n".join(lines)


if __name__ == "__main__":
    print(get_news_summary())
