from fastapi.testclient import TestClient

from apps.site_api.main import app


client = TestClient(app)


def test_site_knowledge_by_stone_library_endpoint_returns_items() -> None:
    response = client.get("/content/knowledge/by-stone-library/9")

    assert response.status_code == 200
    assert response.json() == [{"id": "k1", "title": "Granite Guide", "stone_library_id": 9}]


def test_site_help_center_categories_endpoint_returns_items() -> None:
    response = client.get("/content/help-center/categories")

    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Orders", "is_enabled": True}]
