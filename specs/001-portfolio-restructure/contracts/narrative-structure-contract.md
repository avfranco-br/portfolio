# Interface Contract: Engagement Narrative Heading Structure

**Feature**: Portfolio Look & Feel Restructure  
**Target Files**: `docs/narratives/*.md`

---

## Heading Hierarchy Contract

Every engagement narrative under `docs/narratives/*.md` MUST adhere to the following Markdown heading hierarchy:

```markdown
# [Engagement Title]

[Brief introductory overview paragraph]

## Challenge

[Existing challenge, context, and problem statement paragraphs]

## Approach

[Existing solution architecture, methodology, and execution strategy paragraphs]

## Outcome

[Existing results, business impact, and strategic takeaways paragraphs]
```

### Invariants:
1. `## Challenge`, `## Approach`, and `## Outcome` MUST appear in exact order if present.
2. If a page has no existing prose matching a section, that section heading is omitted (not filled with dummy text).
3. Post-structure word count MUST be $\ge$ pre-structure word count.
