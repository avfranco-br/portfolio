# Spec 002: Custom Domain Migration — alexandrefranco.dev

**Site:** `avfranco-br.github.io/portfolio` (GitHub Pages, MkDocs Material)
**Status:** Ready for implementation (domain registration is a manual prerequisite, see Prerequisites)
**Depends on:** Spec 001 (homepage copy) — not a hard dependency, can run in parallel, but Spec 001 should land first to avoid re-testing the same page twice
**Blocks:** Spec 003+ (any spec assuming the new domain is live)

---

## Context

The portfolio currently resolves at `https://avfranco-br.github.io/portfolio/`, a GitHub-owned subdomain with a subpath. This is being replaced with a dedicated domain, `alexandrefranco.dev`, registered separately (Cloudflare Registrar recommended, since Mostelli's DNS likely already lives there — confirm before starting). This spec covers repo-side GitHub Pages configuration and Cloudflare-side DNS/SSL configuration required for the migration, plus verification steps to confirm the old URL redirects cleanly and HTTPS works without certificate errors.

`alexandrefranco.dev` is an **apex/root domain** (no `www.` or subdomain prefix), which affects which DNS record types are required — this spec assumes apex-only setup. If a `www.alexandrefranco.dev` variant is also wanted, see R7 (optional).

## Goal

1. `alexandrefranco.dev` resolves to the existing GitHub Pages site with a valid HTTPS certificate.
2. The old URL `avfranco-br.github.io/portfolio` continues to work and redirects (or is documented as still-functional) to avoid breaking any existing inbound links (LinkedIn, resume, etc.).
3. DNS and SSL are configured following current best practice for pairing Cloudflare-managed DNS with GitHub Pages, avoiding the common cert-provisioning failure mode this pairing is prone to.

## Non-Goals (explicitly out of scope for this spec)

- Do NOT change any page content (covered by Spec 001 and future specs).
- Do NOT configure email (MX records) for the domain in this spec unless explicitly requested — confirm separately if Alexandre wants email on this domain.
- Do NOT modify Mostelli's or Ideas-to-Life's DNS zones — this spec only touches the new `alexandrefranco.dev` zone.
- Do NOT enable a `www.` subdomain unless R7 is explicitly actioned.

## Prerequisites (manual, human-performed — not for the coding agent)

- [x] `alexandrefranco.dev` registered and active in Cloudflare (confirmed — no registration or nameserver delegation steps needed).
- [ ] Confirm access to the Cloudflare account/zone for the domain before the agent begins DNS steps.
- [ ] Confirm write access to the `avfranco-br/portfolio` GitHub repo settings (Pages configuration requires repo admin).

---

## Division of Work: Agent vs. Manual (GitHub UI)

Confirmed: deployment uses a **GitHub Action** (not `mkdocs gh-deploy` CLI). This affects where the CNAME file needs to live and which steps the coding agent can actually perform versus which require you to click something in the GitHub UI — repo Settings changes generally aren't reachable by a coding agent unless it's been given a token with admin scope, which is not assumed here.

**Agent can do (file/workflow changes, committed via PR or direct commit):**
- R1 — add the `CNAME` file in the correct location for an Actions-based build (see updated R1 below).
- Verify the workflow's build step includes the CNAME file in its output artifact.

**You need to do manually (GitHub web UI, one-time, ~2 minutes):**
- **Settings → Pages → Custom domain**: enter `alexandrefranco.dev` and save. This field is what GitHub actually uses to provision the certificate — the CNAME file alone doesn't fully replace this step for Actions-based deploys, though GitHub will often auto-populate this field from the CNAME file after the first successful deploy. Confirm it's populated; if not, enter it manually.
- **Settings → Pages → Enforce HTTPS**: tick this once GitHub shows the certificate as issued (a padlock/"HTTPS" status will appear next to the domain in that same settings panel). Don't enable before the cert shows as issued — see R4/R5 for why.
- Nothing else on the GitHub side requires manual action if R1–R3 are implemented correctly — Actions handles the actual publish.

**You need to do manually (Cloudflare dashboard):**
- All DNS records in R3.
- Proxy status toggles in R4.
- SSL/TLS mode in R5 (only relevant if you later turn proxying on).
- The TXT verification record in R6.

The agent's role here is limited to the repo-side file change; everything DNS- and settings-panel-related is on you, once, and then it's done.

## Requirements

### R1 — Add CNAME file to repository (GitHub Actions deploy)

Since deployment runs via a GitHub Action (not the `mkdocs gh-deploy` CLI), the CNAME file must end up in the **built site output** that the workflow publishes — not just committed somewhere in the source tree and hoped for.

The reliable approach with MkDocs: place a file named exactly `CNAME` (no extension), containing one line:

```
alexandrefranco.dev
```

...directly inside the `docs/` source directory (i.e. `docs/CNAME`, alongside `docs/index.md`). MkDocs copies all non-Markdown files in `docs_dir` into the built `site/` output by default, so this file will be carried through the build automatically and end up at the root of the published site — which is where GitHub Pages looks for it.

**Verify, don't assume:** check the workflow YAML (likely `.github/workflows/*.yml`) to confirm:
1. The build step actually runs `mkdocs build` (or equivalent) against the `docs/` dir containing this new file.
2. The publish step (commonly `actions/upload-pages-artifact` + `actions/deploy-pages`, or `peaceiris/actions-gh-pages`) uploads the full `site/` build output, not a filtered subset that could exclude the CNAME file.

If the workflow already has a step that copies extra static files separately (some MkDocs setups do this for a `static/` or `assets/` folder outside `docs/`), confirm whichever mechanism is in use will actually include a dotfile-style filename like `CNAME` — some file-copy steps skip dotfiles or extensionless files by default and would need an explicit include rule.

### R2 — Configure GitHub Pages custom domain setting (manual, see Division of Work above)

In the repository's **Settings → Pages**:
- Set the custom domain field to `alexandrefranco.dev`.
- Wait for DNS check to pass (depends on R3 being completed first — GitHub validates DNS before allowing this to save cleanly in some cases, or will show a warning until propagation completes).
- Do **not** enable "Enforce HTTPS" until GitHub shows the certificate as issued (see R5) — enabling it prematurely can cause a temporary broken-HTTPS state.

### R3 — Cloudflare DNS records (apex domain → GitHub Pages)

In the Cloudflare DNS zone for `alexandrefranco.dev`, create the following records. GitHub Pages requires apex domains to point via `A` records (not `CNAME`, since CNAME is not permitted at the zone apex per DNS spec) to GitHub's four load-balanced IPs:

| Type | Name | Content | Proxy status |
|---|---|---|---|
| A | `@` | `185.199.108.153` | DNS only (see R4) |
| A | `@` | `185.199.109.153` | DNS only (see R4) |
| A | `@` | `185.199.110.153` | DNS only (see R4) |
| A | `@` | `185.199.111.153` | DNS only (see R4) |
| AAAA | `@` | `2606:50c0:8000::153` | DNS only (see R4) |
| AAAA | `@` | `2606:50c0:8001::153` | DNS only (see R4) |
| AAAA | `@` | `2606:50c0:8002::153` | DNS only (see R4) |
| AAAA | `@` | `2606:50c0:8003::153` | DNS only (see R4) |

Verify these IPs against GitHub's current published list at implementation time (`https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site`) — GitHub has changed these historically and the agent should not assume the above are still current without checking.

### R4 — Cloudflare proxy status: set to "DNS only" during initial cert issuance

Cloudflare's proxy ("orange cloud") sits in front of GitHub's certificate validation (which uses HTTP-01/ACME challenges) and commonly causes GitHub's automatic Let's Encrypt certificate issuance to fail or hang, because the challenge traffic gets intercepted by Cloudflare's edge instead of reaching GitHub.

- Set all four A records and four AAAA records above to **"DNS only" (grey cloud)**, not proxied, until GitHub confirms the certificate is issued (visible as "HTTPS: Enabled" with a valid cert in repo Settings → Pages).
- Once the certificate shows as issued and "Enforce HTTPS" is successfully enabled on the GitHub side, proxying (orange cloud) **may optionally be turned on** for CDN/DDoS benefits — but this is optional, not required, and reintroduces a small risk of cert renewal issues if GitHub ever needs to re-validate. Recommendation: leave DNS-only unless there's a specific reason to want Cloudflare's proxy features (WAF, caching) for this site.

### R5 — Cloudflare SSL/TLS mode

If proxying is enabled at any point (see R4), set Cloudflare's SSL/TLS encryption mode to **"Full (strict)"**, not "Flexible." Flexible mode causes redirect loops with GitHub Pages because it terminates HTTPS at Cloudflare's edge and connects to GitHub over plain HTTP, which GitHub Pages' own HTTPS-enforcement will then redirect back to HTTPS, looping.

If DNS-only (no proxy, per the R4 recommendation), this setting has no effect and can be left at default.

### R6 — GitHub domain verification (recommended, prevents domain takeover)

Independent of the DNS records above, add GitHub's domain verification TXT record to prove ownership of `alexandrefranco.dev` to GitHub. This is a security best practice that prevents another GitHub user from claiming the domain for a different repository.

- In GitHub: Settings (account-level, not repo-level) → Pages → "Add a domain" → follow the generated TXT record instructions.
- Add the resulting TXT record (format: `_github-pages-challenge-<username>.alexandrefranco.dev` → value provided by GitHub) in Cloudflare DNS.
- Confirm "Verified" status shows in GitHub before considering this spec complete.

### R7 — `www.alexandrefranco.dev`: not in scope

Decided: apex-only. Do not create a `www` CNAME record or any related redirect rule. If this changes in the future, it will be covered by a separate spec.

### R8 — Verify old URL still resolves

After the above is live, confirm `https://avfranco-br.github.io/portfolio/` still loads (GitHub Pages typically continues serving the old path/subdomain unless explicitly disabled). Document the final behavior (does it redirect to the new domain, or serve duplicate content at both URLs?) — if it serves duplicate content at both URLs without a redirect, flag this back for a decision, since it creates a duplicate-content SEO issue that would need a canonical tag or redirect rule to resolve, which is out of scope for this spec.

---

## Acceptance Criteria

- [ ] `https://alexandrefranco.dev` loads the portfolio site with a valid, browser-trusted HTTPS certificate (no security warnings).
- [ ] `http://alexandrefranco.dev` (no S) redirects to `https://alexandrefranco.dev`.
- [ ] GitHub repo Settings → Pages shows the custom domain as verified with HTTPS enforced.
- [ ] All 8 DNS records (4×A, 4×AAAA) are present and correctly pointed per R3.
- [ ] Domain verification TXT record (R6) is added and shows "Verified" in GitHub.
- [ ] Old URL (`avfranco-br.github.io/portfolio`) behavior is confirmed and documented (per R8), even if resolving it is deferred to a follow-up spec.
- [ ] No MX or email-related records were added (confirms Non-Goals honored).

## Rollback

Revert the GitHub Pages custom domain field to blank and remove the `CNAME` file to fall back to the `github.io` URL; Cloudflare DNS records can remain in place harmlessly if rollback is needed, or be removed if the domain purchase itself is being abandoned.

## Decisions Log

- Domain registration: `alexandrefranco.dev` already registered and active in Cloudflare — no delegation steps required.
- `www` subdomain: not wanted, apex-only. R7 updated accordingly.
- Email: not planned on this domain. No MX records in scope for this or any near-term spec; Non-Goals stands.
