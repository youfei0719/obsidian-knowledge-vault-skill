# Vault Structure Reference

Use this reference when initializing or auditing a vault. The structure is intentionally generic and contains no personal data.

## First Principles

1. A saved item is useful only if it can be retrieved later.
2. Retrieval needs context, not only storage.
3. Every card should answer:
   - What is this?
   - Why did it matter?
   - Where does it belong?
   - When should it be reused?
   - What should a future search query find it by?
4. Indexes are part of the product, not housekeeping. They turn a folder of notes into a usable system.

## Recommended Tree

```text
00-收集箱/
01-界面设计/
  交互细节/
  动效/
  按钮/
  组件/
  落地页/
02-代码片段/
  前端/
  后端/
  脚本/
  提示词/
03-Codex能力/
  Skills/
  Agents规则/
  工作流/
04-工具网站/
  在线工具/
  开源项目/
  服务平台/
05-写作素材/
  广告文案/
  微博小红书/
  标题钩子/
  表达句式/
  评论素材/
06-段子梗图/
07-营销案例/
08-产品想法/
09-研究资料/
10-账号人物/
11-可复用模板/
12-工作记录/
  日记录/
  周总结/
  月总结/
99-归档/
_索引/
_模板/
_附件/
```

## Required Indexes

- `_索引/收藏总览.md`: main entry point.
- `_索引/最近收录.md`: chronological feed of new cards.
- `_索引/分类索引.md`: category navigation and category-level card lists.
- `_索引/标签索引.md`: tag-based lookup.
- `_索引/可复用素材.md`: practical material that can be used in projects, writing, design, product, or workflows.
- `_索引/创意线索.md`: material that can inspire new ideas.
- `_索引/工作索引.md`: daily, weekly, monthly, and project work records.
- `_索引/分类变更记录.md`: category additions, moves, merges, and rationale.

## Naming Rules

- Material cards: `clear-title-YYYY-MM-DD.md` or localized equivalent.
- Work records: `YYYY-MM-DD-work-record.md` or localized equivalent.
- Keep titles specific. Avoid `link`, `note`, `untitled`, or serial numbers.
- Preserve technical names when needed, but write the explanation in the user's working language.

## Git Sync Pattern

For a git-backed vault:

1. Pull with rebase before formal collection.
2. Create or update cards and indexes.
3. Stage only intended files.
4. Commit with a meaningful message.
5. Push to remote.

If conflicts occur, preserve both sides and ask for a decision when the merge is not obvious.
