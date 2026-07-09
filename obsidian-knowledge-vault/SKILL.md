---
name: obsidian-knowledge-vault
description: Turn saved links, notes, ideas, snippets, references, and work logs into reusable Obsidian Markdown knowledge cards with Chinese-first or user-language-first metadata, category folders, indexes, reverse lookup, and optional Git sync. Use when the user wants to collect material, save something for later, maintain an Obsidian vault, create searchable knowledge cards, keep daily/weekly/monthly work records, build a personal knowledge base, or query previously saved notes.
---

# Obsidian Knowledge Vault

## Core Idea

Transform capture into retrieval. Do not merely save links or notes. Convert every useful input into a standalone Markdown card with enough context, tags, reuse scenarios, and index entries that it can be found and reused later.

Use three layers:

1. **Capture layer**: accept messy inputs such as links, screenshots, snippets, thoughts, project notes, and work logs.
2. **Processing layer**: classify, summarize, extract value, tag, and turn the item into a card.
3. **Retrieval layer**: update indexes so future questions can find relevant cards by time, category, tag, project, or use case.

## Privacy Rules

- Never publish or sync private vault content unless the user explicitly asks.
- Redact secrets, tokens, private repo names, personal identifiers, private file paths, customer data, and raw work logs from reusable examples.
- Keep source links or original text only when the user provided them for saving and they are appropriate to store.
- If creating a public template or skill from a private vault, extract the workflow and schema only. Do not copy real notes, screenshots, attachments, private indexes, or git history.

## First Step

Before writing, inspect the target vault:

1. Read `AGENTS.md` if present and follow it over this skill.
2. Inspect `_模板/`, `_索引/`, and top-level category folders if they exist.
3. If the vault is missing a structure, offer to initialize one with `scripts/init_vault.py`.
4. If the vault is a git repo, run `git pull --rebase` before collection unless the user asks for local-only work.

## Collection Workflow

Use this flow when the user says things like "save this", "collect this", "this may be useful later", "add to my vault", or provides a link/material to preserve.

1. **Understand the input**
   - Identify type: link, article, tool, code, UI reference, writing material, meme, marketing case, product idea, research, person/account, template, or unknown.
   - Extract source, title, author/platform if available, and original link/content.
   - If information may have changed recently and the user expects accuracy, verify with the web before writing.

2. **Classify conservatively**
   - Prefer an existing category or subfolder.
   - If uncertain, use `00-收集箱/` with status `待判断` and explain the suggested future category.
   - Add a new category only when the type has durable reuse value and cannot fit existing categories.

3. **Create one standalone card**
   - Filename: `中文短标题-YYYY-MM-DD.md` or user-language equivalent.
   - Use Markdown.
   - Include frontmatter fields:
     `标题`, `类型`, `分类`, `来源`, `创建时间`, `标签`, `状态`, `价值评分`, `可用于`, `相关项目`.
   - Include body sections:
     `一句话价值`, `内容摘要`, `为什么值得收藏`, `未来可以怎么用`, `原始内容 / 链接`, `相关联想`, `适合反向调用的场景`.

4. **Update indexes**
   - Always update `_索引/最近收录.md`, `_索引/分类索引.md`, and `_索引/标签索引.md`.
   - Update `_索引/可复用素材.md` when the card has practical reuse value.
   - Update `_索引/创意线索.md` when the card can inspire product, content, design, marketing, or workflow ideas.
   - Update `_索引/分类变更记录.md` when adding, renaming, moving, or merging categories.

5. **Sync if appropriate**
   - If the vault is a git repo and the user expects persistence, stage only intended files, commit with `收录：标题`, and push.
   - If git remote is missing or push fails, keep the local card and tell the user exactly what was not synced.

6. **Reply with result**
   - Title collected
   - Category
   - Card path
   - Indexes updated
   - Git push status

## Work Record Workflow

Use this flow when the user wants daily notes, weekly summaries, monthly reports, or project retrospectives.

1. Decide whether the request is a day record, week summary, month summary, or project review.
2. Write under `12-工作记录/`:
   - `日记录/` for daily records
   - `周总结/` for weekly summaries
   - `月总结/` for monthly summaries
3. For daily records, capture:
   - what was done
   - current progress
   - blockers
   - decisions made
   - follow-ups
   - related projects
4. For weekly/monthly summaries, read the relevant daily records first, then synthesize outcomes, unresolved items, and next focus.
5. Update `_索引/工作索引.md`; if a new card was created, also update `_索引/最近收录.md`.
6. Commit with `工作记录：标题` or `工作总结：标题` when git sync is expected.

## Reverse Lookup Workflow

Use this flow when the user asks what past material can help with a current task.

1. Search indexes first:
   - `_索引/最近收录.md`
   - `_索引/分类索引.md`
   - `_索引/标签索引.md`
   - `_索引/可复用素材.md`
   - `_索引/创意线索.md`
   - `_索引/工作索引.md`
2. Search category folders and relevant cards second.
3. Return useful matches, not just filenames.
4. For each match, explain how it can be reused for the user's current goal.
5. Cite note paths so the user can open the source.

## Category Defaults

Adapt names to the user's language if needed, but keep a stable numbered taxonomy:

- `00-收集箱/`: uncertain, temporary, unclassified
- `01-界面设计/`: UI, pages, buttons, motion, components, interaction details
- `02-代码片段/`: frontend, backend, scripts, prompts, utilities
- `03-Codex能力/`: skills, agent rules, workflows, prompt systems
- `04-工具网站/`: tools, open-source projects, services, platforms
- `05-写作素材/`: copywriting, headlines, phrasing, social posts, ads
- `06-段子梗图/`: memes, jokes, comments, humor
- `07-营销案例/`: brand, campaign, growth, communication cases
- `08-产品想法/`: app ideas, site ideas, features, business models
- `09-研究资料/`: articles, reports, references requiring deeper study
- `10-账号人物/`: creators, accounts, people, personal brands
- `11-可复用模板/`: repeatable structures, methods, templates
- `12-工作记录/`: daily records, weekly summaries, monthly summaries, retrospectives
- `99-归档/`: old or inactive material

## Bundled Resources

- Read `references/vault-structure.md` when setting up a new vault or explaining the system.
- Read `references/templates.md` when writing cards or indexes.
- Run `scripts/init_vault.py /path/to/vault` to create a reusable starter vault skeleton.
