from fastapi.testclient import TestClient

from apps.admin_api.main import app


client = TestClient(app)


def test_admin_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "app": "admin_api"}


def test_error_log_list_endpoint_returns_empty_page_shape() -> None:
    response = client.post("/admin/observability/errors/list", json={})

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}


def test_error_log_detail_endpoint_returns_not_found_for_unknown_id() -> None:
    response = client.get("/admin/observability/errors/1")

    assert response.status_code == 404
    assert response.json()["detail"] == "error log not found"


def test_runtime_log_list_endpoint_returns_empty_page_shape() -> None:
    response = client.post("/admin/observability/runtime/list", json={})

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}


def test_monitors_list_endpoint_returns_empty_page_shape() -> None:
    response = client.post("/admin/observability/monitors/list", json={})

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}


def test_monitor_save_endpoint_returns_saved_payload() -> None:
    payload = {"system_name": "sc-main", "monitor_type": "http", "is_enabled": True}

    response = client.post("/admin/observability/monitors/save", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["system_name"] == "sc-main"
    assert data["monitor_type"] == "http"
    assert data["is_enabled"] is True


def test_audit_list_endpoint_returns_empty_page_shape() -> None:
    response = client.post("/admin/observability/audit/list", json={})

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}
