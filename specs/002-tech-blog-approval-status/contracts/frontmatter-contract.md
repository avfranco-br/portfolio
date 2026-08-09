# Frontmatter Contract: Tech Blog Article Schema

All Markdown files placed in `docs/tech-blog/` MUST conform to this YAML frontmatter contract.

## Schema Definition

```yaml
---
title: "Article Title"
description: "Article description overview."
pubDate: 2026-08-09
status: approved # Allowed: approved | draft | review
tags:
  - agentic-workflows
  - system-architecture
author: "Alexandre Franco"
slug: "article-slug"
target: tech-blog
---
```

## Field Specifications

1. `status` (**Mandatory**):
   - Value: `approved` -> Eligible for publishing in site navigation and index listing.
   - Value: `draft` or `review` -> Excluded from site navigation and public index listing.
   - Omitted -> Interpreted strictly as `draft`.
