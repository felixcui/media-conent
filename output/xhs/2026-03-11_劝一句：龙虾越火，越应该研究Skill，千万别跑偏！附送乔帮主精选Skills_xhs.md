# 🔥 龙虾爆火别跟风！先搞定Skill才是真本事！

✨ 龙虾（OpenClaw）最近火得不像样！
✨ 但很多人装完才发现——没Skill等于空壳！
✨ 今天整理了一份超全Skill清单，建议收藏！

---

## 🎯 核心观点

**没有Skill的龙虾 = 没装App的手机**

龙虾越热，越该沉下心打磨自己的Skill！

---

## 📥 一、抓取采集Skill

### 1️⃣ Agent Reach —— 给AI装眼睛

**GitHub**: `Panniantong/Agent-Reach`

**亮点**：
- 零API成本，让AI访问整个互联网
- 支持小红书、抖音、微信、YouTube、Twitter等
- 本地凭证存储，cookie不外传

**安装**：
```
让AI Agent说："帮我安装 Agent Reach"
https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

---

### 2️⃣ Defuddle —— 网页正文提取神器

**GitHub**: `joeseesun/defuddle-skill`

**亮点**：
- 一键提取干净文章内容
- 自动去除广告、侧边栏
- 返回Markdown + 标题/作者/日期等元数据

**安装**：
```bash
npx skills add joeseesun/defuddle-skill
```

---

### 3️⃣ YouTube搜索下载

**GitHub**: `joeseesun/yt-search-download`

**亮点**：
- YouTube全站搜索 + 视频下载 + 字幕提取
- 最高4K画质，支持MP3音频提取
- 英文标题自动翻译中文

**安装**：
```bash
npx skills add joeseesun/yt-search-download
```

**前置**：YouTube API Key + `brew install yt-dlp`

---

### 4️⃣ Anything to NotebookLM

**GitHub**: `joeseesun/anything-to-notebooklm`

**亮点**：
- 支持15+格式：微信文章、YouTube、PDF、EPUB等
- 自动生成播客、PPT、思维导图、测验

**安装**：
```bash
git clone https://github.com/joeseesun/anything-to-notebooklm.git
cd anything-to-notebooklm
./install.sh
```

---

## ✍️ 二、内容创作Skill

### 5️⃣ 宝玉老师Skill合集

**GitHub**: `jimliu/baoyu-skills`

**亮点**：一个人的内容工厂！
- 小红书信息图、封面图、幻灯片
- X发布、公众号发布、图片压缩

**安装**：
```bash
npx skills add jimliu/baoyu-skills
```

---

### 6️⃣ Markdown一键发X长文

**GitHub**: `joeseesun/qiaomu-x-article-publisher`

**亮点**：
- 写好MD，一键发布X Articles草稿
- 自动处理图片上传，7天免认证

**安装**：
```bash
git clone https://github.com/joeseesun/qiaomu-x-article-publisher.git ~/.claude/skills/qiaomu-x-article-publisher
pip install Pillow pyobjc-framework-Cocoa patchright
python auth_manager.py setup
```

---

### 7️⃣ Knowledge Site Creator

**GitHub**: `joeseesun/knowledge-site-creator`

**亮点**：
- 告诉AI想学什么，自动生成学习网站
- 支持闪卡、测验、进度追踪

**安装**：
```bash
npx skills add joeseesun/knowledge-site-creator
```

---

## ⚡ 三、效率工具Skill

### 8️⃣ Spotify音乐播放器

**GitHub**: `joeseesun/qiaomu-music-player-spotify`

**亮点**：
- 用自然语言控制Spotify
- 5947种音乐风格数据库
- "放点适合写代码的音乐"直接播

**安装**：
```bash
npx skills add joeseesun/qiaomu-music-player-spotify
```

**前置**：需要Spotify Premium账号

---

### 9️⃣ Design Advisor

**GitHub**: `joeseesun/qiaomu-design-advisor`

**亮点**：
- 乔布斯式设计顾问
- 深挖真实用户需求，三层级解决方案

**安装**：
```bash
npx skills add joeseesun/qiaomu-design-advisor
```

---

## 📦 四、Skill管理工具

### 🔧 Skill Publisher —— 发布你的Skill

**GitHub**: `joeseesun/skill-publisher`

自动完成：验证元数据 → 创建GitHub仓库 → 推送代码

```bash
npx skills add joeseesun/skill-publisher
```

---

### 🔍 Find Skills —— 用Skill找Skill

```bash
npx skills add vercel-labs/skills/find-skills
# 然后用 npx skills find react performance 搜索
```

---

## 🌐 更多Skill资源

| 平台 | 网址 | 收录数量 |
|------|------|----------|
| Skills.sh | skills.sh | 86,000+ |
| SkillsMP | skillsmp.com/zh | 38w+ |

---

## 💡 写在最后

**先想清楚：你让AI帮你干什么？**

这个问题想清楚了，Skill自然就知道怎么写了！

---

**喜欢的宝子们点个赞❤️收藏一下！**

**关注我，带你解锁更多AI工具！** 👇

#OpenClaw #Claude #AI编程 #Skills #龙虾 #效率工具 #AI工具