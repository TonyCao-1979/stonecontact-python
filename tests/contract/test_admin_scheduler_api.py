from fastapi.testclient import TestClient

from apps.admin_api.main import app


client = TestClient(app)


def test_scheduler_job_list_endpoint_returns_empty_page_shape() -> None:
    response = client.post("/admin/scheduler/jobs/list", json={})

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}


def test_scheduler_job_detail_endpoint_returns_not_found_for_unknown_id() -> None:
    response = client.get("/admin/scheduler/jobs/1")

    assert response.status_code == 404
    assert response.json()["detail"] == "job not found"


def test_scheduler_job_save_endpoint_returns_saved_payload() -> None:
    payload = {"job_code": "daily_sync", "name": "Daily Sync", "cron_expression": "0 0 * * *"}

    response = client.post("/admin/scheduler/jobs/save", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["job_code"] == "daily_sync"
    assert data["name"] == "Daily Sync"
    assert data["cron_expression"] == "0 0 * * *"
    assert data["is_enabled"] is True


def test_scheduler_enable_endpoint_marks_job_enabled() -> None:
    response = client.put("/admin/scheduler/jobs/1/enable")

    assert response.status_code == 200
    assert response.json()["id"] == "1"
    assert response.json()["is_enabled"] is True


def test_scheduler_disable_endpoint_marks_job_disabled() -> None:
    response = client.put("/admin/scheduler/jobs/1/disable")

    assert response.status_code == 200
    assert response.json()["id"] == "1"
    assert response.json()["is_enabled"] is False


def test_scheduler_run_now_endpoint_returns_queued_result() -> None:
    response = client.post("/admin/scheduler/jobs/1/run-now")

    assert response.status_code == 200
    assert response.json() == {"job_id": "1", "status": "queued"}


def test_scheduler_job_logs_endpoint_returns_empty_page_shape() -> None:
    response = client.get("/admin/scheduler/jobs/1/logs")

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}


def test_scheduler_runtime_state_endpoint_returns_empty_instances() -> None:
    response = client.get("/admin/scheduler/runtime/state")

    assert response.status_code == 200
    assert response.json() == {"instances": []}


def test_scheduler_runtime_triggers_endpoint_returns_empty_page_shape() -> None:
    response = client.get("/admin/scheduler/runtime/triggers")

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}
