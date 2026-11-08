import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="GuildGuide API", version="1.0.0")
FIXTURES = json.loads((Path(__file__).parent.parent / "data" / "demo.json").read_text())

class GuideRequest(BaseModel):
    communityId: str = Field(min_length=1, max_length=80)
    useCase: str = Field(min_length=1, max_length=80)
    budget: int = Field(ge=100, le=20_000)
    maxAgeDays: int = Field(ge=30, le=730)

def generate(request: GuideRequest) -> dict:
    community = next((item for item in FIXTURES["communities"] if item["id"] == request.communityId), None)
    if not community:
        raise HTTPException(status_code=404, detail={"code": "unknown_community", "message": "Choose a known demo community."})
    if request.useCase not in community["useCases"]:
        raise HTTPException(status_code=422, detail={"code": "unsupported_use_case", "message": "Use case is not supported by this community."})
    eligible = [item for item in FIXTURES["products"] if item["communityId"] == request.communityId and item["price"] <= request.budget and request.useCase in item["useCases"]]
    picks = []
    for item in eligible:
        age_score = max(0, 100 - item["reviewedDaysAgo"] / 3)
        score = round(item["fit"] * .5 + item["confidence"] * .3 + age_score * .2)
        picks.append({**item, "score": score, "freshness": "current" if item["reviewedDaysAgo"] <= request.maxAgeDays else "review", "why": f'{item["fit"]}% expert fit · {item["confidence"]}% community confidence · reviewed {item["reviewedDaysAgo"]} days ago'})
    picks.sort(key=lambda item: item["score"], reverse=True)
    queue = [{"id": item["id"], "name": item["name"], "reason": f'Evidence is {item["reviewedDaysAgo"]} days old' if item["reviewedDaysAgo"] > request.maxAgeDays else f'Confidence is only {item["confidence"]}%'} for item in FIXTURES["products"] if item["communityId"] == request.communityId and (item["reviewedDaysAgo"] > request.maxAgeDays or item["confidence"] < 70)]
    return {"communityName": community["name"], "expert": community["expert"], "picks": picks, "queue": queue, "ruleVersion": "2026.11.08"}

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/guides/generate")
def generate_guide(request: GuideRequest): return generate(request)
