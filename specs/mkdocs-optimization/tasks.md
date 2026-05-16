# Tasks: MkDocs & Deployment Optimization

## Phase 1: Configuration & Dependencies
- [x] **Task 1.1**: Update `mkdocs.yml` with `navigation.indexes`.
- [x] **Task 1.2**: Update `mkdocs.yml` with `minify` and `social` plugins.
- [x] **Task 1.3**: Identify required Python packages (`mkdocs-minify-plugin`).

## Phase 2: Workflow Modernization
- [x] **Task 2.1**: Update `deploy.yml` permissions (`pages: write`, `id-token: write`).
- [x] **Task 2.2**: Implement multi-job build and deploy workflow.
- [x] **Task 2.3**: Use `actions/upload-pages-artifact@v3` and `actions/deploy-pages@v4`.

## Phase 3: Validation & Cleanup
- [ ] **Task 3.1**: Run local build to verify minification.
- [ ] **Task 3.2**: Verify social card generation locally.
- [ ] **Task 3.3**: Push changes and monitor GitHub Actions execution.
- [ ] **Task 3.4**: (Backlog) Draft Diátaxis content strategy templates.
