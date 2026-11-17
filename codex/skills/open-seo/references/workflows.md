# Workflow selection

Use the existing MCP tool contracts and project context. Source workflows are optional task-specific references at the pinned revision below; load only the relevant file. Their automatic persistence instructions remain subject to the user's task authorization.

- Keyword research: `research_keywords` for a few seeds, `get_keyword_metrics` for known terms, `get_serp_results` where intent matters. Reuse connected Search Console demand when authorized. Prioritize business fit and intent over volume; confirm market and language. Saving keywords is a separate mutation.
- Competitor and backlink research: discover tools for ranked keywords, competing domains and backlinks; compare the same market and period. Do not infer absent metrics or silently start paid jobs.
- Audits: distinguish crawl findings, Search Console evidence, and provider estimates; establish target scope before fetching a site. The current `seo-audit` workflow calls `whoami` to inspect connection/credits, uses `run_site_audit`, `get_audit_status`, `get_audit_issues`, and `get_audit_pages`, and leaves Lighthouse off unless performance depth was requested. Discover support before calling. A recommendation is not a code change or deploy.
- Ranking evidence: current `get_serp_results` merges three reads. Its row `rank` is not a Google position; use the matching site's `bestPosition` and `seenIn`. A single sighting is unconfirmed, a failed lookup is unknown, and an absent result means only absent within the requested depth. Record query, market, language, observation date and matching URL. Provider traffic is an estimate, not measured visits; same-day variation is not a trend. Prefer connected first-party Search Console evidence where available.
- Reports: synthesize returned evidence, caveats, dates, and next actions. Use the requested destination. Native `seo-report` documents OpenSEO's HTML/report storage contract when saving was requested; public sharing requires explicit authorization.
- Rank tracking, AI visibility, local SEO, and project setup: inspect the corresponding native workflow and actual tool schemas; clarify locations and recurring costs before enabling monitoring.

All twelve official workflow names: `ai-prompt-research`, `ai-visibility-audit`, `competitive-landscape`, `competitor-analysis`, `keyword-clustering`, `keyword-research`, `link-prospecting`, `local-seo`, `seo-audit`, `seo-coach`, `seo-project-setup`, `seo-report`.

Pinned source directory (select the matching subdirectory's `SKILL.md`):
https://github.com/every-app/open-seo/tree/46b815be34723e46ceeefe9b2b907bb62b62fd76/plugins/openseo/skills
