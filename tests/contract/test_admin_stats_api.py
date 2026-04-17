from fastapi.testclient import TestClient

from apps.admin_api.main import app


client = TestClient(app)


def test_traffic_stats_list_endpoint_returns_empty_page_shape() -> None:
    response = client.post("/admin/stats/traffic/list", json={})

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}


def test_business_stats_list_endpoint_returns_empty_page_shape() -> None:
    response = client.post("/admin/stats/business/list", json={})

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}


def test_stats_aggregation_status_endpoint_returns_empty_jobs() -> None:
    response = client.get("/admin/stats/aggregation/status")

    assert response.status_code == 200
    assert response.json() == {"jobs": []}


def test_stats_report_overview_endpoint_returns_empty_metrics() -> None:
    response = client.get("/admin/stats/reports/overview")

    assert response.status_code == 200
    assert response.json() == {"metrics": []}
