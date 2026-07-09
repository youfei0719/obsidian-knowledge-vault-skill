# Templates Reference

Use these templates as defaults. Adapt labels to the user's language and existing vault conventions.

## Collection Card

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

## Work Record Card

```markdown
---
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

- 周总结时直接抽取已完成事项
- 月总结时统计阶段推进
- 回顾某个项目时查看关键节点

## 原始内容 / 链接

## 相关联想

## 适合反向调用的场景
```

## Recent Index Entry

```markdown
- `YYYY-MM-DD HH:mm` [标题](../path/to/card.md) | 分类：`category/path` | 价值：一句话说明未来怎么用。
```

## Category Index Entry

```markdown
- [标题](../path/to/card.md)：说明这张卡适合什么场景，以及为什么值得从该分类中打开。
```

## Tag Index Entry

```markdown
- `标签名`：相关卡片：[[标题一]]、[[标题二]]。适合用于：具体查询或复用场景。
```

## Reusable Material Entry

```markdown
- [标题](../path/to/card.md) | 可用于：场景一、场景二 | 复用方式：具体说明如何拿来用。
```

## Creative Lead Entry

```markdown
- [标题](../path/to/card.md) | 可发散方向：产品功能 / 页面表达 / 内容选题 / 工作流优化。
```
