# CEO review

**Mode:** scope reduction. The initial platform vision is too broad; the accepted scope is one evidence-backed guide workflow and a paid concierge test.

## Premise and alternatives
The user outcome is trusted, current purchase guidance—not “community knowledge management.” Doing nothing wins whenever the owner can tolerate repeat questions, so the ICP must have high-ticket purchases and active experts. The 12-month ideal is a versioned editorial system with proven renewal, not an autonomous ingestion engine.

Alternatives reviewed: concierge-only (fastest proof), maintenance bench + service (chosen), and full ingestion/paywall/affiliate platform (premature). Existing leverage is the community's current threads, experts, identity system, and resource page.

## Eleven-section review
1. **Architecture:** keep fixtures → deterministic ranker → result/review queue as the only demo flow. Defer connectors and persistence.
2. **Errors:** name invalid budget, unknown community, unsupported use case, no eligible product, stale evidence, and internal calculation failure; surface all visibly.
3. **Security:** no user content or credentials. Production requires tenant RBAC, source sanitization, provenance, secret storage, audit logs, and deletion controls.
4. **Data flow:** validate ID/use case/budget/age; filter; score; sort; build queue. Nil, empty, wrong-type, over-limit, stale, and no-match paths are explicit.
5. **Code quality:** one pure ranking contract per runtime, shared fixture, bounded types, no premature repository/service layers.
6. **Tests:** cover successful ranking, budget filtering, stale/dissent queue, invalid inputs, visible loading/empty/error states, flag action, and mobile overflow.
7. **Observability:** production needs guide freshness distribution, generation errors, approval latency, expert churn, affiliate disclosure completeness, and connector health.
8. **State:** demo state is ephemeral. Production needs immutable revisions, uniqueness on tenant/guide/version, and indexes on review due date.
9. **API:** version the contract before external clients; return stable error codes; rate-limit generation and connector sync separately.
10. **Scale:** scoring is small and linear. At 100×, source ingestion and scheduled review fan-out—not ranking—become the bottlenecks.
11. **UX:** show recommendation first, then rationale, freshness, dissent, and action. Never imply simulated ranking is independent testing or live AI.

## Decisions
- **Strongest challenges:** no paid proof, platform bundling, and the expert as a single point of failure.
- **Accepted:** deterministic guide generation, transparent rationale, review queue, one working editorial flag, responsive/accessibility states, concierge validation.
- **Deferred:** authentication, ingestion, live AI, affiliate APIs, payments, persistence, and platform connectors.
- **Not in scope:** scraping private rooms, autonomous publishing, or claiming product testing.
- **Failure line:** do not expand until three owners pay and two experts per community agree to an update SLA.
