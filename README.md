# Obsidian Knowledge Vault Skill

> 用 Codex 把链接、想法、代码、设计参考、写作素材和工作记录，自动整理成可检索、可复用、可反向调用的 Obsidian Markdown 知识卡片。

[English](#english) | [安装](#安装) | [快速开始](#快速开始) | [隐私说明](#隐私说明)

## 这是什么

`obsidian-knowledge-vault` 是一个 Codex Skill，用来把“随手收藏”升级成一套可长期复用的个人知识库工作流。

普通收藏夹只负责存东西。这个 Skill 让 Codex 继续往后做几步：

1. 看懂你丢进来的内容是什么。
2. 判断它应该归到哪个类别。
3. 整理成一张独立的 Obsidian Markdown 卡片。
4. 提炼它为什么值得保存。
5. 标注以后可以怎么复用。
6. 更新最近收录、分类、标签、可复用素材、创意线索等索引。
7. 以后你提问时，从已有卡片和索引里反向找资料。

一句话：它不是帮你“存资料”，而是帮你把资料变成以后真的能找、能用、能复盘的知识资产。

## 适合谁

适合经常积累这些内容的人：

- 设计参考、UI 细节、动效、组件、落地页
- 开源项目、工具网站、软件服务
- 代码片段、脚本、Prompt、Agent 工作流
- 文案、标题、表达句式、社媒素材
- 营销案例、产品想法、研究资料
- 日常工作记录、周总结、月总结、项目复盘

如果你的收藏经常散落在浏览器书签、微信收藏、备忘录、截图和文件夹里，这个 Skill 的目标就是把这些碎片整理成一个稳定的 Obsidian 知识系统。

## 核心能力

### 1. 素材捕获

看到有用的东西，不需要先想文件夹怎么分、标题怎么起、标签怎么写，直接交给 Codex。

可以处理：

- 链接和网页
- 一段文字
- 一个抽象想法
- 一段代码
- 一个工具或开源项目
- 一个 UI / 产品 / 文案参考
- 一条工作记录

### 2. 语义分类

Codex 会根据内容语义判断应该放到哪里，而不是让用户先手动归档。

默认分类：

- `00-收集箱/`：待判断、临时、价值未定内容
- `01-界面设计/`：UI、页面、按钮、动效、组件、交互细节
- `02-代码片段/`：前端、后端、脚本、提示词
- `03-Codex能力/`：Skills、Agent 规则、工作流、提示词系统
- `04-工具网站/`：工具、开源项目、软件、服务平台
- `05-写作素材/`：文案、标题、表达、社媒、广告
- `06-段子梗图/`：段子、梗、评论、搞笑素材
- `07-营销案例/`：品牌、传播、广告、热点案例
- `08-产品想法/`：App 想法、网站想法、功能灵感、商业模式
- `09-研究资料/`：文章、报告、资料、深度研究
- `10-账号人物/`：博主、账号、人物、创作者案例
- `11-可复用模板/`：结构、方法、模板
- `12-工作记录/`：日记录、周总结、月总结、工作复盘
- `99-归档/`：历史或低频内容

这些目录只是默认模板，可以按你的语言、领域和使用习惯修改。

### 3. 知识卡片化

每条新内容都会变成一张独立 Markdown 卡片，而不是只保存一个链接。

默认卡片结构：

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

这张卡片的重点不是“记录发生了什么”，而是保留未来检索和复用需要的信息。

### 4. 多维索引维护

Skill 会指导 Codex 更新这些索引：

- `_索引/收藏总览.md`
- `_索引/最近收录.md`
- `_索引/分类索引.md`
- `_索引/标签索引.md`
- `_索引/可复用素材.md`
- `_索引/创意线索.md`
- `_索引/工作索引.md`
- `_索引/分类变更记录.md`

索引是这套系统的关键。没有索引，Obsidian 只是文件夹；有了索引，资料才会变成可以被反向调用的知识库。

### 5. 反向知识检索

以后不用手动翻收藏夹，可以直接问 Codex：

- 我最近收藏了哪些东西？
- 我收藏过哪些 UI 设计参考？
- 这个项目能用哪些旧资料？
- 找 5 个能用于广告文案的素材。
- 有没有之前存过的产品功能灵感？
- 我这周都做了哪些工作？
- 帮我从工作记录里整理月报。

Codex 会优先查索引，再查具体卡片，并说明每条资料可以怎么用于当前任务。

### 6. 工作记录沉淀

这套结构也支持工作记录：

- 日记录
- 周总结
- 月总结
- 项目复盘

每天只要简单记录做了什么，后面写周报、月报、复盘时就不用靠记忆硬想。

## 工作原理

这套工作流分成三层：

```text
输入层：素材捕获 / 工作记录捕获 / 来源保留
处理层：语义分类 / 知识卡片化 / 价值提炼 / 复用场景标注
调用层：标签体系 / 多维索引 / 反向知识检索 / Git 同步备份
```

如果配合 Git 使用，链路可以理解为：

```text
Codex 负责理解和整理
Obsidian 负责阅读和长期保存
GitHub 负责同步和备份
```

## 安装

克隆仓库：

```bash
git clone https://github.com/youfei0719/obsidian-knowledge-vault-skill.git
```

复制 Skill 到 Codex 技能目录：

```bash
mkdir -p ~/.codex/skills
cp -R obsidian-knowledge-vault-skill/obsidian-knowledge-vault ~/.codex/skills/
```

重启 Codex，让它重新发现 Skill。

## 快速开始

### 初始化一个新的 Obsidian Vault

Skill 内置了一个初始化脚本，可以创建通用知识库骨架：

```bash
python3 ~/.codex/skills/obsidian-knowledge-vault/scripts/init_vault.py ~/ObsidianKnowledgeVault
```

然后用 Obsidian 打开 `~/ObsidianKnowledgeVault`。

如果你想用 Git 备份：

```bash
cd ~/ObsidianKnowledgeVault
git init
git add .
git commit -m "初始化 Obsidian 知识库"
```

之后可以创建一个私有 GitHub 仓库并推送，或者使用你自己的同步方案。

### 保存一个链接

```text
Use $obsidian-knowledge-vault.
收录这个链接到我的 Obsidian Vault：
https://example.com
```

Codex 应该会完成：

1. 理解链接内容。
2. 判断分类。
3. 创建 Markdown 卡片。
4. 更新相关索引。
5. 如果 Vault 使用 Git，同步提交并推送。

### 保存一个想法

```text
Use $obsidian-knowledge-vault.
这个以后可能用得上：
做一个把日常工作记录自动整理成月报的工具。
```

### 记录工作

```text
Use $obsidian-knowledge-vault.
工作记录：今天完成了 onboarding 页面，修了两个 bug，并整理了发布说明。
```

### 反向检索

```text
Use $obsidian-knowledge-vault.
从我之前收藏的内容里，找一些能帮助我设计 SaaS dashboard 的参考。
```

## 推荐使用方式

日常使用时可以把 Codex 当成资料管理员：

1. 看到有用内容，直接发给 Codex。
2. 让 Codex 生成一张独立卡片。
3. 让 Codex 更新索引。
4. 开始新项目、写文案、做设计、写总结时，直接问过去有哪些素材能用。
5. 定期用工作记录生成周总结或月总结。

## 隐私说明

这个仓库只包含通用 Skill、通用模板和初始化脚本，不包含任何私人 Vault 内容。

如果你要基于自己的知识库发布类似项目，请务必先移除：

- 真实笔记
- 截图和附件
- 私有仓库名
- 本地绝对路径
- Token、Key、密码和 Cookie
- 个人身份信息
- 客户、公司、项目或工作敏感内容
- 原始工作记录和内部复盘

建议只发布：

- 工作流规则
- 通用目录结构
- 通用模板
- 初始化脚本
- 脱敏后的示例

## 仓库结构

```text
obsidian-knowledge-vault/
  SKILL.md
  agents/
    openai.yaml
  references/
    templates.md
    vault-structure.md
  scripts/
    init_vault.py
```

## 设计原则

- 先卡片，后索引。
- 先复用价值，后归档洁癖。
- 不确定分类时，先进收集箱。
- 每条内容都要解释未来怎么用。
- 反向查询时，优先查索引，再查原始卡片。
- 私人内容和公开模板必须严格分离。

## License

MIT

---

## English

`obsidian-knowledge-vault` is a Codex Skill for turning captured material into reusable Obsidian Markdown knowledge cards.

It helps Codex:

- capture links, notes, snippets, ideas, references, and work logs
- classify them into a stable vault structure
- create standalone Markdown cards
- extract why each item matters
- describe future reuse scenarios
- update indexes for retrieval
- support reverse lookup later
- optionally sync the vault with Git

Install:

```bash
git clone https://github.com/youfei0719/obsidian-knowledge-vault-skill.git
mkdir -p ~/.codex/skills
cp -R obsidian-knowledge-vault-skill/obsidian-knowledge-vault ~/.codex/skills/
```

Initialize a starter vault:

```bash
python3 ~/.codex/skills/obsidian-knowledge-vault/scripts/init_vault.py ~/ObsidianKnowledgeVault
```

Example prompt:

```text
Use $obsidian-knowledge-vault.
Save this link into my Obsidian vault:
https://example.com
```

This repository contains only generic workflow rules, templates, and scripts. It does not include private vault content.
