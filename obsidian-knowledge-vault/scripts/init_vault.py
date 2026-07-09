#!/usr/bin/env python3
"""Initialize a generic Obsidian knowledge vault skeleton."""

from __future__ import annotations

import argparse
from pathlib import Path


DIRS = [
    "00-收集箱",
    "01-界面设计/交互细节",
    "01-界面设计/动效",
    "01-界面设计/按钮",
    "01-界面设计/组件",
    "01-界面设计/落地页",
    "02-代码片段/前端",
    "02-代码片段/后端",
    "02-代码片段/脚本",
    "02-代码片段/提示词",
    "03-Codex能力/Skills",
    "03-Codex能力/Agents规则",
    "03-Codex能力/工作流",
    "04-工具网站/在线工具",
    "04-工具网站/开源项目",
    "04-工具网站/服务平台",
    "05-写作素材/广告文案",
    "05-写作素材/微博小红书",
    "05-写作素材/标题钩子",
    "05-写作素材/表达句式",
    "05-写作素材/评论素材",
    "06-段子梗图",
    "07-营销案例",
    "08-产品想法",
    "09-研究资料",
    "10-账号人物",
    "11-可复用模板",
    "12-工作记录/日记录",
    "12-工作记录/周总结",
    "12-工作记录/月总结",
    "99-归档",
    "_索引",
    "_模板",
    "_附件/网页快照",
    "_附件/图片",
    "_附件/项目备份",
]


FILES = {
    "README.md": """# Obsidian Knowledge Vault

This vault turns captured material into reusable Markdown cards.

Start from `_索引/收藏总览.md`.
""",
    "_模板/收藏卡片.md": """---
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
""",
    "_模板/工作记录卡片.md": """---
标题: ""
类型: "工作记录"
分类: "12-工作记录/日记录"
来源: ""
创建时间: ""
标签: ["工作记录", "日记录"]
状态: "收集"
价值评分: 4
可用于: ["周总结", "月总结", "项目复盘"]
相关项目: []
---

# 标题

## 一句话价值

## 内容摘要

- 今天做了什么
- 推进到了哪一步
- 当前还卡在哪里

## 为什么值得收藏

## 未来可以怎么用

## 原始内容 / 链接

## 相关联想

## 适合反向调用的场景
""",
    "_索引/收藏总览.md": """# 收藏总览

优先从最近收录、分类索引、标签索引、可复用素材和创意线索进入。

- [[最近收录]]
- [[分类索引]]
- [[标签索引]]
- [[可复用素材]]
- [[创意线索]]
- [[工作索引]]
""",
    "_索引/最近收录.md": """# 最近收录

## 条目
""",
    "_索引/分类索引.md": """# 分类索引

## 当前分类总览

- `00-收集箱/`：待判断、临时、价值未定内容
- `01-界面设计/`：UI、页面、按钮、动效、组件、交互细节
- `02-代码片段/`：前端、后端、脚本、提示词
- `03-Codex能力/`：Skills、Agents 规则、工作流
- `04-工具网站/`：工具、开源项目、服务平台
- `05-写作素材/`：文案、标题、表达、评论素材
- `06-段子梗图/`
- `07-营销案例/`
- `08-产品想法/`
- `09-研究资料/`
- `10-账号人物/`
- `11-可复用模板/`
- `12-工作记录/`
- `99-归档/`

## 分类下素材
""",
    "_索引/标签索引.md": """# 标签索引

## 标签
""",
    "_索引/可复用素材.md": """# 可复用素材

## 条目
""",
    "_索引/创意线索.md": """# 创意线索

## 条目
""",
    "_索引/工作索引.md": """# 工作索引

## 快速入口

- [日记录目录](../12-工作记录/日记录)
- [周总结目录](../12-工作记录/周总结)
- [月总结目录](../12-工作记录/月总结)

## 最近工作记录

## 最近工作总结
""",
    "_索引/分类变更记录.md": """# 分类变更记录

## 记录
""",
    "AGENTS.md": """# Obsidian Knowledge Vault Rules

Use this vault to turn external material into searchable, reusable Markdown cards.

## Default workflow

1. Pull latest changes if this is a git repo.
2. Classify the input.
3. Create one standalone Markdown card.
4. Update indexes.
5. Commit and push when sync is expected.

## Privacy

Do not publish private notes, secrets, personal identifiers, or raw work logs.
""",
}


def write_file(path: Path, content: str, overwrite: bool) -> bool:
    if path.exists() and not overwrite:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize an Obsidian knowledge vault skeleton.")
    parser.add_argument("vault_path", help="Target vault directory")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing template/index files")
    args = parser.parse_args()

    root = Path(args.vault_path).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    for rel in DIRS:
        (root / rel).mkdir(parents=True, exist_ok=True)

    written = 0
    skipped = 0
    for rel, content in FILES.items():
        if write_file(root / rel, content, args.overwrite):
            written += 1
        else:
            skipped += 1

    print(f"Initialized vault: {root}")
    print(f"Directories ensured: {len(DIRS)}")
    print(f"Files written: {written}")
    print(f"Files skipped: {skipped}")


if __name__ == "__main__":
    main()
