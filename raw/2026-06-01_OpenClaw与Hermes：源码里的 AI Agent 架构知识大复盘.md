---
title: "OpenClaw与Hermes：源码里的 AI Agent 架构知识大复盘"
author: "rianli"
source: "腾讯程序员 / 腾讯技术工程"
date: "2026-05-29"
url: "https://mp.weixin.qq.com/s/49dxdMXEUoWIYlIh8fFqMQ"
collected: "2026-06-01"
---

# OpenClaw与Hermes：源码里的 AI Agent 架构知识大复盘

> 腾讯程序员 / 腾讯技术工程 · rianli · 2026-05-29

## 文章概述

本文从源码层面深入剖析 OpenClaw（TypeScript 微内核架构）和 Hermes Agent（Python 单体架构）两大 AI Agent 框架的设计哲学与工程取舍。作者在开发 QQ Bot 插件的过程中通读了 OpenClaw 核心源码，对两个框架的认知经历了"看山三境"的完整过程。

**三部分结构：**
- **Part I**：OpenClaw 源码拆解 — 设计原理、Gateway 中枢、插件系统（25+ Channel Adapter）、Agent 执行引擎、记忆系统、安全机制
- **Part II**：Hermes Agent 源码拆解 — 单体 AIAgent 类、ToolRegistry 自注册、MemoryManager + 8 插件、技能自创建闭环、Smart Approval 三态安全
- **Part III**：正面对比 + 第 22 章（7+1 节）— 协议互通、记忆分层、上下文工程（融合 Anthropic 上下文焦虑症理论）、能力管理、确定性编排、多 Agent 协作（GAN-like 架构）、Harness 全链路治理、沙箱安全

## 核心观点

### 哲学差异
- **OpenClaw = 平台架构师的范本**：微内核 + Plugin SDK 强契约，边界 vs 实现分离，核心代码几千行，能力靠插件叠出。适合多团队协作、长期演进、多租户 SaaS
- **Hermes = 个人开发者的瑞士军刀**：单体 + ToolRegistry 自注册 + 技能自创建闭环。一个人能看完代码、改核心、加工具，反馈闭环极短。适合个人助手、研究原型
- **共同点**：两个框架都把记忆当成长期投入的主战场，投入的设计复杂度远超大多数 Agent 框架

### OpenClaw 四大设计回答
1. **多协议可插拔契约**：Channel 25+ Adapter，Per-channel Streaming，Cross-channel Docking
2. **LLM 上下文资源预算**：可插拔 Context Engine + 三级 Compaction（Pre-request / Timeout-triggered / Overflow）+ Bootstrap Budget
3. **记忆自动沉淀不退化**：Dreaming 三阶段加权晋升（Light → REM → Deep）
4. **凭证失败与业务失败分治**：Auth Profile（13 种 FailoverError 闭合枚举）+ 持久化冷却状态

### Hermes 三大启示
1. **经验自动复用**：技能自创建闭环 + 改进闭环 + 渐进式披露（目录名 → 元数据 → 完整指令）
2. **安全审批先 LLM 分诊再叫人**：Smart Approval 三态（Default/Auto/Plan）
3. **执行隔离覆盖本地到云端**：8 种沙箱后端（Local/Docker/SSH/Modal/Daytona/Singularity/Vercel/Managed Modal）

### 双向连接架构
OpenClaw 可同时扮演四种协议角色：MCP Server（工具粒度）、ACP Server（Agent 粒度）、HTTP API（系统粒度）、WebSocket。CLI Backend 双路径：能把 Claude Code/Codex CLI 当 backend 用（反向 MCP 注入工具），也能被它们当 backend 调。

### 第 22 章：超越框架的延伸思考（7+1 方向）
1. **协议互通（22.1）**：ACP/MCP/A2A 已就绪，缺编排层
2. **记忆分层（22.2）**：情景/语义/程序性三类记忆 + 千人千面 + 遗忘机制
3. **上下文工程（22.3）**：Anthropic"上下文焦虑症"——35分钟/80K-150K tokens 开始退化；上下文重置 vs 压缩；两阶段 Session 轮换；结构化 Handoff
4. **能力管理（22.4）**：Skill 渐进式披露 + 云端 Skill 体系
5. **确定性编排（22.5）**：已验证流程从 Skill 固化为 Workflow
6. **多 Agent 协作（22.6）**：Anthropic GAN-like Planner/Generator/Evaluator 架构 + Sprint Contract；字节 Eino 的 Graph 编排 + DeepAgent + Transfer + Checkpoint
7. **Harness 全链路治理（22.7）**：自我评估偏差的对抗性消除；三阶段治理（执行前拦截 → 执行中约束 → 执行后验证）；"缩小依赖模型自觉性的面积"
8. **沙箱安全（22.8）**：安全边界推到离用户最近的地方

### Google《Agentic Design Patterns》21 模式对照
Auth Profile + FailoverError → Exception Handling and Recovery
Plugin SDK + Channel Adapter + CLI Backend → Tool Use + MCP + Inter-Agent Communication
Dreaming 三阶段 → Memory Management + Learning and Adaptation
Smart Approval → Human-in-the-Loop（LLM 分诊版）
GAN-like 架构 → Multi-Agent + Reflection + Evaluation
**共同空白**：Goal Setting and Monitoring（只到预算层）、对抗性评估缺失、Exploration and Discovery 不在产品定位

## 参考引用
- OpenClaw: https://github.com/openclaw/openclaw
- Hermes Agent: https://github.com/NousResearch/hermes-agent
- Agentic Design Patterns（中文版）: https://github.com/xindoo/agentic-design-patterns
- Anthropic Harness Engineering (2026.03): GAN-like 多智能体、上下文焦虑症、Sprint Contract
- Chroma Research Context Rot (2025): 18 模型上下文退化实证
- OpenHarness (HKUDS): 轻量级 Agent Harness 框架
- Eino (字节 CloudWeGo): Go 语言 LLM 应用框架，多 Agent 编排
