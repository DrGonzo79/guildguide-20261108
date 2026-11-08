# Phased build prompts

1. Add tenant-scoped Postgres models for guides, immutable revisions, sources, expert approvals, votes, and review deadlines; preserve the deterministic rule contract.
2. Add one read-only connector behind a kill switch. Store source provenance and consent; never scrape private rooms or publish without approval.
3. Add AI-assisted claim extraction with citations, confidence, and a mandatory human approval queue. Test hallucinated/missing sources.
4. Add community SSO/paywall adapters, exports, disclosure reporting, connector telemetry, and incident runbooks only after paid renewal.
