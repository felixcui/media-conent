#!/usr/bin/env python3
"""
AI 资讯获取与分类脚本 V4 最终版
使用智谱 AI 进行智能分类
"""
import requests
import json
import os
from datetime import datetime, timedelta

# 需要过滤的标题关键词（直接跳过，不进入分类）
EXCLUDED_TITLE_KEYWORDS = [
    "招聘", "诚聘", "招贤", "加入我们", "简历", "猎头",
]

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
ZHIPU_BASE_URL = "https://open.bigmodel.cn/api/coding/paas/v4"


def classify_with_ai(news_list):
    """使用智谱 AI 进行智能分类"""
    
    if not news_list:
        return {}
    
    print(f"🤖 使用智谱 AI 分类 {len(news_list)} 条资讯...")
    
    # 准备资讯标题列表
    news_text = "\n".join([f"{i+1}. {item['title']}" for i, item in enumerate(news_list)])
    
    prompt = f"""请对以下 {len(news_list)} 条资讯进行智能分类。

分类规则（严格使用以下6个分类名称）：

**AI编程与开发** 💻 - 编程工具、软件开发、工程实践、软件工程、研发效能、DevOps、架构设计、工程规范、代码审查、测试部署
**AI模型与技术** 🧠 - 模型发布、技术突破、算法研究
**AI内容创作** 🎨 - AI生成内容、创意工具、创作应用
**AI产品与应用** 🚀 - AI产品、企业应用、行业落地
**AI行业动态** 📈 - 融资、人事、公司动态、行业事件
**观点与趋势** 💡 - 观点、趋势分析、深度思考
**其他** 📂 - 仅限完全无法归类的非AI内容，尽量少用此分类

⚠️ 重要：宁可归入最接近的AI相关分类，也不要归入「其他」。所有与AI、科技、互联网相关的内容都应归入上面6个分类。

请以 JSON 格式输出，格式如下：
{{"AI编程与开发": [0, 3, 5], "AI模型与技术": [1, 2], ...}}

待分类资讯：
{news_text}"""
    
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
                    model="glm-5-turbo",
                    messages=[
                        {"role": "system", "content": "分类助手，只输出JSON。"},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.1,
                    max_tokens=16384
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
                        "AI编程与开发": "AI编程与开发",
                        "AI模型与技术": "AI模型与技术",
                        "AI内容创作": "AI内容创作",
                        "AI产品与应用": "AI产品与应用",
                        "AI行业动态": "AI行业动态",
                        "观点与趋势": "观点与趋势",
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
                if isinstance(idx, int) and 0 <= idx < total_count:
                    classified_indices.add(idx)

    if len(classified_indices) == total_count:
        return categories

    missing = [i for i in range(total_count) if i not in classified_indices]
    if missing:
        if "其他" not in categories:
            categories["其他"] = []
        categories["其他"].extend(missing)

    return categories


def classify_by_keywords(news_list):
    """智能关键词分类方案（6分类新版）"""
    classified_indices = set()
    categories = {
        "AI编程与开发": [],
        "AI模型与技术": [],
        "AI内容创作": [],
        "AI产品与应用": [],
        "AI行业动态": [],
        "观点与趋势": [],
        "其他": [],
    }

    rules = [
        ("AI编程与开发", [
            "Vibe Coding", "Claude Code", "Cursor", "GitHub Copilot",
            "编程助手", "代码生成", "IDE插件", "智能编程", "编程技巧",
            "软件工程", "工程规范", "工程实践", "研发效能", "DevOps", "CI/CD", "代码审查",
            "编码代理", "AI编码", "编程代理", "编码工具", "开源项目",
            "架构设计", "测试", "部署", "Harness", "Agent Harness",
            "从没写过代码", "干掉了一个估算团队",
        ]),
        ("AI模型与技术", [
            "新论文", "论文", "顶会", "CVPR", "ICLR", "AAAI", "NeurIPS", "ICML",
            "模型架构", "算法", "推理优化", "微调", "蒸馏", "量化",
            "多模态", "Transformer", "Benchmark", "评测",
            "性能直逼", "模型发布", "版本更新", "能力提升",
        ]),
        ("AI内容创作", [
            "短剧", "视频生成", "AI视频", "AI绘画", "AI写作",
            "图像生成", "内容创作", "创作工具", "生成式",
            "Seedance", "Sora", "Midjourney", "Stable Diffusion",
            "做AI视频", "AI做视频", "视频制作", "内容生产",
        ]),
        ("AI行业动态", [
            "融资", "投资", "万美元", "亿人民币", "估值", "IPO", "上市",
            "裁员", "入职", "离职", "人事变动", "任命", "辞职",
            "收购", "并购", "加入", "联手", "合作",
            "战争", "杀入", "砸", "亿", "战略", "布局",
            "创业者", "独角兽", "巨头",
        ]),
        ("观点与趋势", [
            "观点", "趋势", "观察", "思考", "分析",
            "未来", "预测", "影响", "变革", "重塑",
            "我却", "想要", "感想", "随笔",
            "改造", "需要的不止是", "的边界",
        ]),
        ("AI产品与应用", [
            "发布会", "正式发布", "上线", "推出",
            "开卖", "送到", "正式", "答案", "方案",
            "落地", "实践", "业务", "应用",
            "Agent", "智能体", "SaaS", "平台",
            "实测", "体验", "试用", "评测",
            "Skill", "技能", "知识库", "教程", "保姆级",
        ]),
    ]

    non_ai_keywords = [
        "招聘", "诚聘", "招贤", "加入我们", "简历",
        "直播预告", "预告", "倒计时", "敬请期待",
    ]

    for i, news in enumerate(news_list):
        if i in classified_indices:
            continue

        title = news["title"]
        classified = False

        for keyword in non_ai_keywords:
            if keyword in title:
                categories["其他"].append(i)
                classified_indices.add(i)
                classified = True
                break

        if classified:
            continue

        for category, keywords in rules:
            for keyword in keywords:
                if keyword in title:
                    categories[category].append(i)
                    classified_indices.add(i)
                    classified = True
                    break
            if classified:
                break

        if not classified:
            if any(x in title for x in ["编码", "编程", "代码", "开源项目"]):
                categories["AI编程与开发"].append(i)
                classified_indices.add(i)
            elif any(x in title for x in ["模型架构", "算法创新", "Benchmark", "论文", "顶会"]):
                categories["AI模型与技术"].append(i)
                classified_indices.add(i)
            elif any(x in title for x in ["发布", "上线", "推出", "实测", "体验"]):
                categories["AI产品与应用"].append(i)
                classified_indices.add(i)
            elif any(x in title for x in ["视频", "图像", "绘画", "写作", "创作", "生成"]):
                categories["AI内容创作"].append(i)
                classified_indices.add(i)
            elif any(x in title for x in ["融资", "投资", "收购", "上市", "亿"]):
                categories["AI行业动态"].append(i)
                classified_indices.add(i)
            else:
                categories["AI产品与应用"].append(i)
                classified_indices.add(i)

    return categories


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
                        # 过滤招聘类文章
                        if any(kw in title for kw in EXCLUDED_TITLE_KEYWORDS):
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
        print(f"🔍 智谱 API Key: {ZHIPU_API_KEY[:6]}...{ZHIPU_API_KEY[-4:]}")
        print(f"🔍 智谱 Base URL: {ZHIPU_BASE_URL}")
        print(f"🔍 模型: glm-5-turbo")
        
        categories = classify_with_ai(news_list)
        
        # 统计分类结果
        total_classified = sum(len(v) for v in categories.values())
        print(f"📊 分类完成统计: 总计 {len(news_list)} 条, 已分类 {total_classified} 条")
        for cat, items in categories.items():
            if items:
                print(f"  - {cat}: {len(items)} 条")
        
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
    
    ai_news_count = sum(len(indices) for indices in categories.values())
    
    if ai_news_count == 0:
        lines.append("😊 暂无AI相关资讯～")
        lines.append("")
        return "\n".join(lines)
    
    category_order = [
        "AI编程与开发",
        "AI模型与技术",
        "AI内容创作",
        "AI产品与应用",
        "AI行业动态",
        "观点与趋势",
        "其他"
    ]
    
    for category in category_order:
        if category not in categories or not categories[category]:
            continue
            
        indices = categories[category]
        lines.append(f"### {category}（{len(indices)} 条）")
        lines.append("")
        
        for i, idx in enumerate(indices, 1):
            if idx < 0 or idx >= len(news_list):
                continue
            news = news_list[idx]
            title = news["title"]
            link = news["link"]
            biz_name = news.get("biz_name", "")
            
            if biz_name:
                lines.append(f"{i}. [{title}]({link}) `{biz_name}`")
            else:
                lines.append(f"{i}. [{title}]({link})")
        
        lines.append("")
    
    return "\n".join(lines)


if __name__ == "__main__":
    print(get_news_summary())
