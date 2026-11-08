# GuildGuide

A runnable vertical-slice prototype for maintained, expert-reviewed buying guides inside paid enthusiast communities. It ranks fictional products against a budget and use case, shows source provenance and dissent, expires stale evidence, and creates an editorial review queue.

**Live frontend:** https://drgonzo79.github.io/guildguide-20261108/  
**Source idea:** https://www.ideabrowser.com/hub/ideas/today

All communities, products, rankings, and editorial signals are fictional demo fixtures. No platform, affiliate, AI, or member data is accessed. The FastAPI backend is runnable/tested source and is **not publicly deployed**.

## Run

Requires Node 24.22.2 and Python 3.12+.

```bash
npm ci
npm run dev

uv sync --project api --locked --dev
uv run --project api uvicorn api.main:app --reload
```

## Verify

```bash
npm run typecheck
npm run test:e2e
npm run build
npm audit --audit-level=high
uv run --project api pytest api/tests
```

## Domain contract

`POST /guides/generate` validates a known community, supported use case, $100–$20,000 budget, and 30–730 day freshness policy. It returns ranked eligible products, transparent scoring, provenance, dissent, and a maintenance queue. Invalid input is rejected; no-match returns an honest empty list.

See `docs/PRODUCT.md`, `docs/ARCHITECTURE.md`, `docs/OFFICE_HOURS.md`, `docs/CEO_REVIEW.md`, and `docs/BUILD_PROMPTS.md`.
