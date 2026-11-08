# Product plan

## ICP and JTBD
**ICP:** owner of a 100–1,000 member, $10K+/month paid enthusiast community with frequent $300+ purchase decisions, an existing recommendation page, and two credible experts.

**JTBD:** “When a member asks what to buy, publish a current recommendation with the reasoning, source discussion, dissent, expert sign-off, and next review date—without rebuilding the answer every week.”

## MVP and data model
The MVP selects a fictional community and use case, applies a budget and maximum review age, ranks products with a deterministic scoring contract, exposes stale/contested evidence, and creates a maintenance queue. Users can inspect the reasoning and flag a recommendation for review.

- `Community`: vertical, owner, currency, editorial policy.
- `ProductEvidence`: price, use cases, expert fit, confidence, cited thread, review date, dissent.
- `GuideRequest`: community, use case, budget, maximum evidence age.
- `GuideResult`: ranked picks, rationale, freshness state, queue, rule version.
- Future: tenant-scoped `Guide`, `Revision`, `ExpertApproval`, `Vote`, `Source`, and immutable `Publication`.

## Architecture and model strategy
The static Next.js app imports explicit JSON fixtures and executes the deterministic TypeScript contract. The tested FastAPI endpoint reads the same fixture and mirrors ranking/validation. Production makes FastAPI canonical, adds Postgres, tenant-scoped RBAC, scheduled review jobs, provenance hashes, and connector adapters.

AI may later extract candidate claims from threads and draft summaries, but it cannot approve a recommendation, fabricate a citation, or hide disagreement. Every claim needs a source, expert identity, review date, and deterministic freshness status.

## Economics, validation, moat
- Offer: free teardown → $1,500 setup → $149/month software + $400/month expert retainer → optional 10% affiliate GMV.
- Report model: 25 year-one customers, ~$37.5K setup revenue, ~$13.7K exit MRR, roughly $120K booked; conversion assumptions remain unvalidated.
- Demand gate: 20 Looms → ≥5 owner calls → ≥3 deposits. Kill or remain a service if fewer than three deposits.
- Metrics: repeat-question reduction, guide-open-to-affiliate-click, review SLA, stale-guide count, disputed recommendation rate, expert retention, and paid renewal.
- Moat: reviewed recommendation history, source-linked disagreement, expert workflow, and vertical-specific editorial data—not a generic page builder.

## Risks
Native bundling, expert churn, cold-outbound fatigue, affiliate-conflict distrust, and stale advice are existential. Mitigations are two experts per community, visible commercial disclosures, expiry by default, exports, and a concierge-first sales motion.

## 30 / 60 / 90 days
- **30:** send 20 teardowns, observe five real update sessions, collect three deposits, manually produce 30 guides.
- **60:** measure maintenance time and member usage across three communities; build approvals and review reminders only if usage recurs.
- **90:** add one connector and affiliate disclosure reporting only after 70% weekly editor activation and two renewals; otherwise keep it a service or stop.
