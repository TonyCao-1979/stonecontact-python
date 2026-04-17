from fastapi.testclient import TestClient

from apps.admin_api.main import app


client = TestClient(app)


def test_admin_knowledge_item_update_endpoint_returns_ok() -> None:
    payload = {"item_id": 1, "title": "Granite Guide", "content": "Updated content"}

    response = client.post("/admin/content/knowledge/items/update", json=payload)

    assert response.status_code == 200
    assert response.json() == {"ok": True, "item_id": 1}


def test_admin_help_center_article_update_endpoint_returns_ok() -> None:
    payload = {"article_id": 3, "title": "FAQ", "content": "Updated article"}

    response = client.post("/admin/content/help-center/articles/update", json=payload)

    assert response.status_code == 200
    assert response.json() == {"ok": True, "article_id": 3}
