# Harness Engineering: How to Build AI Workflows That Never Fall Apart

**作者**: mirku (@mirku21)

**来源**: https://x.com/mirku21/status/2098836008468992471?s=46

---

## 摘要

文章指出，AI工作流失败通常并非模型能力不足，而是执行环境即“harness”设计不当；与其反复修改提示词或更换模型，不如构建可靠的外部基础设施。Harness engineering关注模型读取什么、可调用哪些工具、上下文重置后保留哪些数据以及何时停止执行，并通过环境与记忆、工具与权限、验证与反馈三层结构，让同一模型在受控系统中稳定完成复杂任务。

---

## 正文

Most people respond to a broken AI output by rewriting the prompt

Then they switch models

Then they upgrade to a larger context window

The model still forgets instructions

It still recommends the wrong tool

It still skips verification

It still claims success on broken work

The problem sits outside the model weights

The problem sits in the execution environment

That environment is the harness

Designing it is harness engineering

Dario Amodei explained this directly during the launch of Claude Code:

"Of course, you need an interface, you need a harness to use them"

The model acts as a reasoning engine

A model can predict the next logical step

It cannot build a stable operating system on its own

The harness controls what the model reads, what tools it can trigger, what data survives context resets, and when the execution must halt

Prompt engineering adjusts the wording

Harness engineering builds the infrastructure where that wording executes

Put a frontier model in an empty chat box, and it generates casual prose

Put that identical model in a repository with terminal access, automated test suites, project maps, and isolated workspaces, and it ships working software

The weights stay identical

The harness changes everything

OpenAI recorded the identical pattern when training agents on Codex

Their early runs failed because the environment was underspecified

The engineering team avoided asking the model to try harder

They built explicit capability checks and mechanical boundaries

When an agent fails repeatedly, stop editing adjectives in the system prompt

Inspect the operating system around the model

# The Three Layers of a Reliable AI System

Builders often treat prompt chains, agent loops, and multi-agent graphs as competing ideas

They represent three distinct layers of one system

## 1. The Harness Layer (Environment and Memory)

The harness consists of everything existing outside model weights

It manages filesystem access, environment variables, authentication tokens, and durable files

Andrej Karpathy established the defining mental model:

The model is the CPU

The context window is the RAM

A raw CPU without storage or an operating system crashes instantly

When users dump twenty pages of background text into a single prompt, they flood the RAM

The model loses attention on critical rules

A clean harness stores project knowledge in external markdown files

It loads only the exact snippet needed for the immediate step

## 2. The Loop Layer (Evidence and Convergence)

A model outputting code or text needs automated validation

Asking the model "Are you sure this is right?" creates a circular hallucination loop

The model evaluates its own probabilistic prediction and confirms its initial bias

The loop layer introduces objective sensors:

- Test runners (pytest, vitest, cargo test)

- Format validators (JSON schema checkers, linters)

- Execution budgets (maximum four attempts before human review)

The model suggests the correction

The harness runs the test and supplies the raw terminal output

Execution continues only when mechanical evidence confirms the fix

## 3. The Graph Layer (Work Allocation)

Long tasks crumble when forced into a single endless conversation thread

The graph layer distributes work across isolated execution contexts

One worker analyzes the task and writes an implementation blueprint

A second worker writes the code in an isolated directory branch

A third adversarial worker reviews the diff against project requirements

Context stays clean

No single prompt carries the burden of the entire project lifecycle

# The 5 Core Jobs of a Personal AI Harness

You do not need a massive enterprise platform to apply harness engineering

A personal harness requires five mechanical rules in your everyday workflows

## 1. Turn Every Request into a Bounded Contract

Conversational prompts allow models to silently redefine success

When an ambiguous prompt encounters friction, the model solves an easier adjacent task and reports victory

A production contract sets hard boundaries before generation starts:

- Deliverable: Exact file name and format

- Constraints: Dependencies allowed, style requirements, token budget

- Non-Goals: Explicit list of items the model must avoid touching

- Acceptance Criteria: The exact condition required to close the task

Without an explicit contract, the model decides when it finishes

With a contract, the criteria decides when the model finishes

## 2. Provide a Map, Not an Encyclopedia

Context degradation strikes every frontier model over long horizons

Dumping an entire project documentation file into chat burns tokens and dilutes focus

Elite builders create a compact root map

The map outlines where documentation, schemas, and source files live

The model scans the map, selects the single relevant file, and reads that file alone

A compact map preserves working memory

A giant prompt dump exhausts it

## 3. Externalize Memory into Durable Files

Chat history serves as temporary scratch space

The conversation thread is not a database

When a session runs long, attention fades and context windows fill up

Store architecture decisions, user preferences, and unresolved bugs in a dedicated project file

In Claude Code and Cursor, this file is `CLAUDE.md` or `.cursorrules`

When starting a fresh session, the model reads the file and resumes immediately

The work survives chat wipes, rate limits, and model switches

## 4. Build Sensors Before Granting Autonomy

An agent cannot repair errors it cannot observe

Telling a model "write bug-free code" changes nothing

Providing a command that outputs exit code zero or a stack trace gives the model ground truth

Sensors turn subjective quality into verifiable evidence:

- Compilers and type checkers that fail on syntax errors

- Automated test scripts that verify data transformations

- Checklist validators that confirm all required fields exist

The model creates the artifact

The sensor generates the evidence

The harness decides if the run passes

## 5. Apply the Dual-Encoding Rule

Writing a rule in plain English leaves room for probabilistic failure

The model reads the instruction, parses twenty other constraints, and skips the rule under load

Dual-encoding solves this permanently:

First, explain the rule in text so the model understands the goal

Second, place a mechanical gate that blocks execution if the rule breaks

If an agent must avoid deleting files, tell it in the prompt

Then restrict its terminal permissions so `rm -rf` throws an operating system error

The prompt guides the intention

The mechanical gate protects the system

# How to Set Up a Personal Micro-Harness

Here is a five-minute harness structure you can paste into any repository, Claude Project, or Cursor workspace

Save this content as `HARNESS.md` in your project root:

This short file replaces twenty lines of repetitive prompting in every chat

It establishes project scope, controls file access, and forces mechanical verification

# The Two-Pass Prompting Workflow

When working on difficult reasoning tasks in standard chat interfaces, use a two-pass harness loop

Most users ask for an answer and accept the first draft

Production workflows split generation and critique into separate passes

## Pass 1: The Execution Pass

## Pass 2: The Adversarial Review Pass

Separating the creator role from the reviewer role cuts hallucinated claims in half

The model cannot defend its own errors when explicitly instructed to attack them

# Why the Harness Compounds

Models update every few months

Prompts that work today often produce different outputs on the next model checkpoint

Harness engineering preserves your engineering effort

When Anthropic releases an updated Claude or OpenAI launches a new reasoning model, your prompts might require minor adjustments

Your test suites, project maps, permission boundaries, and durable state files remain intact

They work on the new model immediately

The model provides raw cognitive compute

The harness provides the rails that turn compute into reliable execution

Stop tweaking adjectives in your prompts

Start building the harness around them

---
📊 互动数据：❤️ 478 | 🔁 50 | 👁 1490444 | 🔖 1679