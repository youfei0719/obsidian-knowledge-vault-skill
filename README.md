# Obsidian Knowledge Vault Skill

An open-source Codex Skill for turning links, notes, ideas, code snippets, UI references, writing material, and work logs into reusable Obsidian Markdown cards.

The core idea is simple:

> Do not use AI only to save information. Use AI to make information retrievable and reusable.

This skill helps Codex act like a knowledge-vault operator:

- capture messy input
- classify it
- turn it into a standalone Markdown card
- extract why it matters
- mark how it can be reused
- update indexes
- support reverse lookup later
- optionally sync the vault through Git

No private vault content is included in this repository. The workflow is abstracted into a reusable template.

## What It Can Do

### 1. Material Capture

Save anything that may be useful later:

- links and webpages
- tools and open-source projects
- UI references
- code snippets
- prompts and agent workflows
- writing material
- marketing cases
- product ideas
- research material
- creators or accounts
- reusable templates

### 2. Semantic Classification

Codex decides where the item belongs instead of forcing you to choose a folder first.

Default categories include:

- `00-收集箱/`
- `01-界面设计/`
- `02-代码片段/`
- `03-Codex能力/`
- `04-工具网站/`
- `05-写作素材/`
- `06-段子梗图/`
- `07-营销案例/`
- `08-产品想法/`
- `09-研究资料/`
- `10-账号人物/`
- `11-可复用模板/`
- `12-工作记录/`
- `99-归档/`

You can rename these categories for your own language or domain.

### 3. Knowledge Card Creation

Every saved item becomes a standalone Markdown card with metadata and reusable context:

```markdown
---
标题: ""
类型: ""
分类: ""
来源: ""
创建时间: ""
标签: []
状态: "收集"
价值评分: 3
可用于: []
相关项目: []
---

# 标题

## 一句话价值

## 内容摘要

## 为什么值得收藏

## 未来可以怎么用

## 原始内容 / 链接

## 相关联想

## 适合反向调用的场景
```

### 4. Index Maintenance

The skill tells Codex to update:

- `_索引/最近收录.md`
- `_索引/分类索引.md`
- `_索引/标签索引.md`
- `_索引/可复用素材.md`
- `_索引/创意线索.md`
- `_索引/工作索引.md`
- `_索引/分类变更记录.md`

These indexes are what make the vault useful later.

### 5. Reverse Knowledge Lookup

Instead of searching through old bookmarks manually, you can ask:

- "What have I saved recently?"
- "Which saved UI references can help this project?"
- "Find five saved materials I can use for ad copy."
- "What old notes can help with this product idea?"
- "What did I work on this week?"
- "Summarize my month from my work records."

Codex should search indexes first, then source cards, and explain how each result can be reused.

### 6. Work Record System

The same vault can store:

- daily work records
- weekly summaries
- monthly summaries
- project retrospectives

This makes weekly reports and monthly reports much easier because the raw work trail is already structured.

## Installation

Clone this repository:

```bash
git clone https://github.com/youfei0719/obsidian-knowledge-vault-skill.git
```

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R obsidian-knowledge-vault-skill/obsidian-knowledge-vault ~/.codex/skills/
```

Restart Codex so it can discover the new skill.

## Optional: Initialize a New Vault

The skill includes a helper script that creates a generic starter Obsidian vault structure.

```bash
python3 ~/.codex/skills/obsidian-knowledge-vault/scripts/init_vault.py ~/ObsidianKnowledgeVault
```

Open `~/ObsidianKnowledgeVault` in Obsidian.

If you want Git sync:

```bash
cd ~/ObsidianKnowledgeVault
git init
git add .
git commit -m "初始化 Obsidian 知识库"
```

Then create a private GitHub repo and push it, or use your preferred sync method.

## How To Use

### Save a Link

```text
Use $obsidian-knowledge-vault.
Save this link into my Obsidian vault:
https://example.com
```

Codex should:

1. understand the link
2. classify it
3. create a Markdown card
4. update indexes
5. commit and push if your vault uses Git

### Save an Idea

```text
Use $obsidian-knowledge-vault.
This idea may be useful later:
An app that turns daily work notes into monthly reports.
```

### Record Work

```text
Use $obsidian-knowledge-vault.
Work record: today I finished the onboarding flow, fixed two bugs, and drafted the release notes.
```

### Ask For Reverse Lookup

```text
Use $obsidian-knowledge-vault.
Find saved materials that can help me design a SaaS dashboard.
```

## Recommended Daily Workflow

1. Send anything useful to Codex.
2. Let Codex write one card per item.
3. Let Codex update the indexes.
4. Ask reverse-lookup questions when starting new work.
5. Use daily work records as raw material for weekly and monthly summaries.

## Privacy Guidance

Before publishing your own version of this workflow:

- remove real notes
- remove screenshots
- remove attachments
- remove private repo names
- remove tokens, keys, and credentials
- remove personal identifiers
- remove client or employer data
- keep only templates, folder structure, and workflow rules

This repository follows that rule: it contains only the reusable skill and generic starter templates.

## Repository Layout

```text
obsidian-knowledge-vault/
  SKILL.md
  agents/openai.yaml
  references/
    templates.md
    vault-structure.md
  scripts/
    init_vault.py
```

## License

MIT
