from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_ranks_eligible_products_and_builds_queue():
    response = client.post("/guides/generate", json={"communityId":"lens-lab","useCase":"travel","budget":1500,"maxAgeDays":90})
    assert response.status_code == 200
    body = response.json()
    assert body["picks"][0]["name"] == "Lumina X4"
    assert all(item["price"] <= 1500 for item in body["picks"])
    assert any(item["name"] == "Ember GX" for item in body["queue"])

def test_returns_empty_instead_of_inventing_pick():
    response = client.post("/guides/generate", json={"communityId":"lens-lab","useCase":"portrait","budget":100,"maxAgeDays":90})
    assert response.status_code == 200
    assert response.json()["picks"] == []

def test_unknown_community_has_named_error():
    response = client.post("/guides/generate", json={"communityId":"missing","useCase":"travel","budget":1500,"maxAgeDays":90})
    assert response.status_code == 404
    assert response.json()["detail"]["code"] == "unknown_community"

def test_invalid_budget_is_rejected():
    response = client.post("/guides/generate", json={"communityId":"lens-lab","useCase":"travel","budget":0,"maxAgeDays":90})
    assert response.status_code == 422

def test_unsupported_use_case_is_rejected():
    response = client.post("/guides/generate", json={"communityId":"lens-lab","useCase":"commute","budget":1500,"maxAgeDays":90})
    assert response.status_code == 422
    assert response.json()["detail"]["code"] == "unsupported_use_case"
