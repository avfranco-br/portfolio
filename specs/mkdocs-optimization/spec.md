# Feature Specification: MkDocs & Deployment Optimization

**Feature Branch**: `feat/optimize-mkdocs-deploy-modernization`  
**Created**: 2026-05-16  
**Status**: Approved  
**Input**: Optimize MkDocs configuration for best practices and modernize the GitHub Pages deployment workflow.

## User Scenarios & Testing

### User Story 1 - Professional Portfolio Polish (Priority: P1)

As a visitor to the portfolio, I want to see rich previews (social cards) and experience fast page loads (minification) so that the site feels professional and modern.

**Why this priority**: Core value of a portfolio is presentation and performance.

**Independent Test**: Verify that social cards are generated in `site/` and HTML/JS/CSS files are minified after build.

**Acceptance Scenarios**:

1. **Given** a build is triggered, **When** the `minify` plugin is active, **Then** output files in `site/` should be significantly smaller and stripped of comments/whitespace.
2. **Given** a page is shared on social media, **When** the `social` plugin is active, **Then** a preview card should be generated.

---

### User Story 2 - Modern & Secure Deployment (Priority: P1)

As the site owner, I want to use the latest GitHub Actions deployment method (artifacts) so that I don't have to manage a `gh-pages` branch and the deployment is more secure.

**Why this priority**: Eliminates technical debt (branch pollution) and aligns with GitHub's best practices.

**Independent Test**: Successfully deploy the site to GitHub Pages without a `gh-pages` branch.

**Acceptance Scenarios**:

1. **Given** a push to `main`, **When** the `deploy.yml` workflow runs, **Then** it should upload a build artifact and trigger the `deploy-pages` action.

---

## Requirements

### Functional Requirements

- **FR-001**: Enable `navigation.indexes` for improved site structure.
- **FR-002**: Enable `minify` plugin for build-time optimization.
- **FR-003**: Enable `social` plugin for OpenGraph metadata generation.
- **FR-004**: Replace branch-based deployment with artifact-based deployment in GitHub Actions.
- **FR-005**: Use OIDC (id-token) for secure deployment permissions.

## Success Criteria

### Measurable Outcomes

- **SC-001**: Deployment completes successfully using `actions/deploy-pages@v4`.
- **SC-002**: `site/` directory contains minified assets.
- **SC-003**: Social preview images are present in the build output.

## Assumptions

- The environment has access to standard GitHub Actions features.
- The `mkdocs-material` theme is used (verified).
- Python 3.12 is available in CI.
