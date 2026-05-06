# Cursor团队把内部开发流程打包成插件：18个技能+2个规则+1个代理

**作者**: winkrun

**来源**: https://mp.weixin.qq.com/s/nlt4vgE1UptWNvOaZvleWQ

---

## 摘要

Cursor团队将其内部开发流程打包成cursor-team-kit插件，在Cursor中输入特定命令即可即插即用且无需第三方集成。该套件包含18个技能、2个规则和1个代理，技能覆盖了CI监控与修复、PR评审与清理、代码去杂乱等全流程开发场景，规则侧重TypeScript类型安全与代码规范，代理则负责监控CI运行状态，旨在帮助开发者直接复用高效工作流以提升工程化效率。

---

## 正文

winkrun winkrun

在小说阅读器读本章

去阅读

Cursor团队将内部工作流打包成插件，通过 `/add-plugin cursor-team-kit` 即可安装。该套件设计为即插即用，无需第三方服务集成，包含18个技能、2个规则和1个代理。

## 完整组件列表

### 技能（Skills）

| 技能 | 描述 |
| --- | --- |
| `loop-on-ci` | 监控CI运行并迭代修复失败，直到检查通过 |
| `review-and-ship` | 运行结构化评审、提交更改并打开PR |
| `pr-review-canvas` | 生成交互式HTML PR步骤指导，带注释分类diff |
| `verify-this` | 使用基线/处理证据证明或否让主张 |
| `control-cli` | 构建或适配本地驱动器来驱动交互式CLI或TUI |
| `control-ui` | 构建或适配本地浏览器/CDP驱动器处理Web或Electron UI |
| `make-pr-easy-to-review` | 清理杂乱PR历史，改进描述并添加评审指导 |
| `run-smoke-tests` | 运行Playwright热身测试并分类失败 |
| `fix-ci` | 查找失败CI任务，检查日志并应用重点修复 |
| `new-branch-and-pr` | 创建新分支、完成工作并打开提取请求 |
| `get-pr-comments` | 获取并总结活跃PR的评审评论 |
| `check-compiler-errors` | 运行编译和类型检查命令并报告失败 |
| `what-did-i-get-done` | 总结指定时间段内的作者提交，生成简洁状态更新 |
| `weekly-review` | 生成周度回顾，高亮bug修复/技术债/新功能 |
| `fix-merge-conflicts` | 解决合并冲突，验证构建/测试并总结决策 |
| `deslop` | 移除AI生成的代码杂乱并清理代码风格 |
| `workflow-from-chats` | 从聊天中提取持久工作偏好到技能、规则或文档 |

### 代理（Agents）

| 代理 | 描述 |
| --- | --- |
| `ci-watcher` | 监控GitHub Actions运行并返回简洁的通过/失败总结 |

### 规则（Rules）

| 规则 | 描述 |
| --- | --- |
| `typescript-exhaustive-switch` | 要求对联合/枚举进行穷尽切换处理 |
| `no-inline-imports` | 保持import在模块顶层以便可读性和一致性 |

## 安装方式

Cursor中直接使用命令： `/add-plugin cursor-team-kit`

插件地址：https://cursor.com/marketplace/cursor/cursor-team-kit

关注公众号回复“进群”入群讨论。

继续滑动看下一个

AI工程化

向上滑动看下一个

微信扫一扫  
使用小程序

： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过