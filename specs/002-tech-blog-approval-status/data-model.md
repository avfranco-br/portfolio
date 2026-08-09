# Data Model: Tech Blog Approval Status Publishing Filter

## Entities & Schemas

### 1. TechnicalArticle (Markdown Frontmatter)

Represents an individual technical blog post file located under `docs/tech-blog/*.md`.

| Field | Type | Required | Allowed Values | Description |
|-------|------|----------|----------------|-------------|
| `title` | String | Yes | Non-empty text | Title of the technical article |
| `pubDate` | Date | Yes | `YYYY-MM-DD` | Publication date |
| `status` | Enum | Yes | `approved`, `draft`, `review` | Publication approval status |
| `tags` | List[String] | No | Text tags | Categorization tags |
| `author` | String | Yes | Author name | Article author |
| `slug` | String | Yes | Kebab-case string | URL slug identifier |
| `target` | String | No | `tech-blog` | Target taxonomy section |

#### Validation Rules:
- If `status` is missing, null, or any value other than `approved`, the article is classified as `unapproved` (`draft`).
- Only articles with `status: approved` are published to `mkdocs.yml` navigation and `docs/tech-blog/index.md`.

### 2. TechBlogIndex (Listing View)

Represents the aggregated overview page at `docs/tech-blog/index.md`.

| Field | Type | Description |
|-------|------|-------------|
| `approved_posts` | List[TechnicalArticle] | List of articles ordered by `pubDate` descending where `status == 'approved'` |
