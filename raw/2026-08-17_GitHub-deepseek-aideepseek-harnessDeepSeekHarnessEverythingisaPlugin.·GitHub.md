# GitHub - deepseek-ai/deepseek-harness: DeepSeek Harness: Everything is a Plugin. · GitHub

**来源**: https://github.com/deepseek-ai/deepseek-harness

---

## 摘要

DeepSeek Harness（dsh）是DeepSeek AI开发的一款开源智能体框架，其核心特色是采用“万物皆插件”的架构，并由Cordis驱动。该项目目前处于开发者预览阶段，后续可能会有破坏性更新。用户可通过npm或从源码克隆的方式安装并启动Web UI。此外，项目遵循MIT开源协议，积极鼓励社区反馈、插件开发与交流协作。

---

## 正文

DeepSeek Harness English | 中文 DeepSeek Harness ( dsh ) is an open-source agent harness developed by DeepSeek AI . It uses an architecture where everything is a plugin , and is powered by Cordis , whose design is described in A Programming Paradigm for Spatiotemporal Composability . Developer preview DeepSeek Harness is currently in developer preview and is iterating rapidly. THERE WILL BE COMPATIBILITY-BREAKING CHANGES. Run Run from npm Install Node.js , then run: npx @deepseek-ai/dsh web The command starts the Web UI, served at http://127.0.0.1:3080 by default. See Web UI guide . Run from source To run from a repository checkout: git clone https://github.com/deepseek-ai/deepseek-harness.git cd deepseek-harness pnpm install pnpm run build pnpm dsh web Community and support Feel free to submit feedback or bug reports through GitHub Discussions . Add the dsh-plugin topic to your plugin repository for discoverability. Join DeepSeek Harness Discord community . Contributing See CONTRIBUTING.md . Development Start with the development guide and architecture documentation . For agents, follow AGENTS.md . License MIT Third-party dependencies and their licenses are disclosed in THIRD_PARTY_NOTICES.md .