---
name: wechat-to-xiaohongshu
description: 将公众号文章保存到本地并转换为小红书风格文案，统一存储到输出目录下
---

# 公众号文章转小红书文案

将公众号文章保存到输出目录，然后转换为小红书风格文案也存储到同一目录，保持内容精华的同时适配小红书的内容呈现方式。

## 参数

- `$ARGUMENTS`: 公众号文章的 URL（必填），以及可选的输出目录路径

## 输出目录

输出目录按以下优先级确定（从高到低）：

| 优先级 | 方式 | 示例 |
|--------|------|------|
| 1 | 用户在参数中明确指定目录 | `/wechat-to-xiaohongshu <URL> --output-dir ~/Desktop/xhs` |
| 2 | 默认：skill 内部的 `output/` 子目录 | `wechat-to-xiaohongshu/output/` |

> 执行前，先向用户确认使用何种输出目录，若用户未特别说明则使用默认目录。

## 执行步骤

### 步骤 0：确定输出目录

根据上方优先级规则确定 `$OUTPUT_DIR`：
- 若用户指定了目录，使用用户指定的路径（支持 `~` 和相对路径）
- 否则默认为：`<本 SKILL.md 所在目录>/output/`（即 `wechat-to-xiaohongshu/output/`）

确保目录存在：
```bash
mkdir -p "$OUTPUT_DIR"
```

### 步骤 1：保存公众号文章

使用 `wechat-url-to-markdown` skill 抓取并保存文章内容到输出目录：

```bash
python <wechat-url-to-markdown skill 路径>/scripts/save_wechat.py "$ARTICLE_URL" -o "$OUTPUT_DIR"
```

文章将保存为：`$OUTPUT_DIR/YYYY-MM-DD_文章标题.md`

### 步骤 2：读取保存的文章

从输出目录读取刚保存的 Markdown 文件，提取内容用于转换。

### 步骤 3：分析文章结构

提取文章的核心要素：
- **标题**: 吸引眼球的亮点
- **痛点**: 问题或需求
- **核心内容**: 3-5 个关键要点
- **价值**: 读者能获得什么
- **行动号召**: 引导互动

### 步骤 4：转换文案风格

按照小红书内容特点进行转换：

#### 结构模板

```markdown
# 🔥 吸引眼球的标题（使用emoji）

✨ 开头钩子（引起共鸣）
✨ 提出问题
✨ 引出下文

---

## 🎯 核心内容

### 1️⃣ 要点一
- 关键信息
- 实用技巧

### 2️⃣ 要点二
- 关键信息
- 实用技巧

### 3️⃣ 要点三
- 关键信息
- 实用技巧

---

## 💡 实用总结/行动建议

---

## 📝 互动引导

**喜欢的宝子们点个赞❤️收藏一下！**

**关注我，带你解锁更多XX内容！** 👇

#话题标签1 #话题标签2 #话题标签3
```

#### 文案风格要求

1. **标题**: 🔥 emoji + 痛点/亮点 + 情绪词
2. **开头**: 3-5 个钩子句，使用 ✨ emoji
3. **正文**:
   - 分点阐述，每点使用 emoji 数字标记
   - 简洁有力，避免冗长
   - 重点内容加粗或使用特殊符号
4. **结尾**: 互动引导 + 关注引导
5. **标签**: 3-5 个相关话题标签

### 步骤 5：保存小红书文案

将生成的小红书文案保存到 `$OUTPUT_DIR` 目录。

**文件名格式**: `YYYY-MM-DD_文章标题_xhs.md`

**文件内容结构**:
```markdown
---
title: "小红书文案标题"
source: "原文标题"
author: "公众号作者"
date: "YYYY-MM-DD"
original_url: "微信公众号链接"
tags: ["标签1", "标签2", "标签3"]
---

# 小红书文案内容...
```

**保存操作**:
```bash
# 写入文件（$OUTPUT_DIR 已在步骤 0 创建）
cat > "$OUTPUT_DIR/YYYY-MM-DD_文章标题_xhs.md" << 'EOF'
$XHS_CONTENT
EOF
```

### 步骤 6：输出结果

告知用户两个文件的保存位置（均在同一目录下）：
1. 原文保存路径: `$OUTPUT_DIR/YYYY-MM-DD_文章标题.md`
2. 小红书文案保存路径: `$OUTPUT_DIR/YYYY-MM-DD_文章标题_xhs.md`

## 内容转换原则

### 精简原则
- 删除冗余表述，保留核心信息
- 每个要点不超过 3 句话
- 使用短句和短语，提高可读性

### 情感化表达
- 使用"宝子们"、"家人们"等亲切称呼
- 添加"超赞"、"必看"、"神器"等情绪词
- 使用感叹号增强语气

### 视觉优化
- 合理使用 emoji 分隔内容
- 使用引用块、列表等格式
- 段落之间保持适当间距

## 常用 emoji 组合

- **开头**: ✨ 🔥 💡 📢 🎯
- **要点**: 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣
- **强调**: 💪 ⚡ 🌟 💎 🚀
- **总结**: 📝 ✅ 💡 🎁
- **结尾**: ❤️ 👇 📌

## 示例

### 输入
```bash
/wechat-to-xiaohongshu https://mp.weixin.qq.com/s/xxxxx
# 或指定输出目录
/wechat-to-xiaohongshu https://mp.weixin.qq.com/s/xxxxx --output-dir ~/Desktop/xhs
```

### 输出

**文件已保存（默认目录）:**

1. **原文**: `wechat-to-xiaohongshu/output/2026-01-28_文章标题.md`
2. **小红书文案**: `wechat-to-xiaohongshu/output/2026-01-28_文章标题_xhs.md`

**小红书文案预览:**
```markdown
# 🔥 Claude Code神器推荐！让AI变成你的项目经理！

✨ 还在为AI代码质量不稳定发愁？
✨ 还在担心漏掉关键功能？
✨ 还在想怎么把AI能力沉淀下来？

今天给大家安利一款宝藏工具——Superpowers！

---

## 🎯 什么是Superpowers？

简单说，它是一个**强制性的软件开发工作流**！

装上之后，Claude Code会被约束在标准流程里：
```
讨论需求 → 写计划 → 写代码 → 自己审查
```

不再是"拿到任务就开干"，而是像有个项目经理在旁边管着它！👨‍💼

---

## 💪 三大核心命令

| 命令 | 作用 |
|------|------|
| `/superpowers:brainstorm` | 项目启动前先头脑风暴 |
| `/superpowers:write-plan` | 创建详细实现计划 |
| `/superpowers:execute-plan` | 分批执行，带审查检查点 |

---

## 💡 核心价值

**防止遗漏 + 强制规范**

每次使用Claude Code的工作都会以skill的形式沉淀和积累下来！📚


#ClaudeCode #AI编程 #Superpowers #Skills #编程工具 #开发效率
```

## 文件存储结构

```
wechat-to-xiaohongshu/
└── output/                           # 默认输出目录（建议加入 .gitignore）
    ├── YYYY-MM-DD_文章标题.md          # 公众号原文
    └── YYYY-MM-DD_文章标题_xhs.md      # 小红书文案
```

## 注意事项

- 保持原内容的核心价值不变
- 字数严格控制在 1000 字以内
- 标签要与内容高度相关
- 避免过度营销化，保持内容真实
- 技术类内容保持专业性，不过度娱乐化
- **输出目录**：默认为 `wechat-to-xiaohongshu/output/`，可在调用时通过 `--output-dir` 参数自定义
