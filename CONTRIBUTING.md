# Contributing / 贡献指南

本仓库是一个公开的双语合规知识库。提交内容前，请确保材料已经脱敏，并且所有重要结论都有可访问的来源。

## 文档要求

- 一条主题使用稳定 ID，并维护 zh-CN 与 en-US 两个版本。
- 每篇文档标注平台、地区、证据等级、来源更新时间、知识库核查日期和下次复核日期。
- 区分官方规则、官方操作说明、监管要求、执行建议和社区经验。
- 不复制第三方项目的代码或长篇原文；使用自己的摘要，并链接到原始来源。
- 不把社区案例、内部经验或法律意见写成 Apple 或 Google 的强制要求。
- 对冲突、翻译滞后、页面不可访问和历史要求进行明确说明。

## 提交流程

1. 先更新对应语言文件。
2. 检查中英文主题是否配对。
3. 检查来源链接和日期。
4. 运行 scripts/validate_kb.py。
5. 在提交说明中写明影响的平台、地区和主题。

## Issue templates and validation

Use the repository issue forms when possible:

- [New knowledge-base topic](.github/ISSUE_TEMPLATE/new-topic.yml)
- [Source refresh](.github/ISSUE_TEMPLATE/source-refresh.yml)
- [Translation review](.github/ISSUE_TEMPLATE/translation-review.yml)

Before opening a pull request, run:

```bash
python scripts/validate_kb.py
mkdocs build --strict
```

A current source URL may be recorded in front matter or in the page body; normative pages must expose an official Markdown source link. Paired pages must keep the same stable ID, platform, authority, and status.

## 内容安全

不得提交账号、密码、访问令牌、客户数据、内部 App 细节、未公开漏洞或未经批准的法律意见。发现敏感信息时，请停止提交并联系仓库维护者。
