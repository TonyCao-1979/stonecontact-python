from fastapi.testclient import TestClient

from apps.admin_api.main import app


client = TestClient(app)


def test_file_upload_endpoint_returns_upload_result() -> None:
    payload = {"scheme": "product", "file_name": "stone.jpg", "business_module": "stone_library"}

    response = client.post("/admin/file/upload", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["relative_path"].endswith("stone.jpg")
    assert data["public_url"] is None


def test_file_batch_upload_endpoint_returns_items() -> None:
    payload = {
        "files": [
            {"scheme": "product", "file_name": "a.jpg"},
            {"scheme": "product", "file_name": "b.jpg"},
        ]
    }

    response = client.post("/admin/file/upload/batch", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 2
    assert data["total"] == 2


def test_file_download_endpoint_returns_resolved_file() -> None:
    response = client.get("/admin/file/download", params={"relative_path": "product/stone.jpg"})

    assert response.status_code == 200
    assert response.json() == {
        "relative_path": "product/stone.jpg",
        "content_type": None,
        "size": None,
    }


def test_file_delete_endpoint_returns_deleted_path() -> None:
    response = client.request("DELETE", "/admin/file", json={"relative_path": "product/stone.jpg"})

    assert response.status_code == 200
    assert response.json() == {"relative_path": "product/stone.jpg", "deleted": True}


def test_file_copy_endpoint_returns_new_target_path() -> None:
    payload = {
        "source_path": "product/source.jpg",
        "target": {"scheme": "product", "file_name": "target.jpg"},
    }

    response = client.post("/admin/file/copy", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["relative_path"].endswith("target.jpg")


def test_image_process_endpoint_returns_variants() -> None:
    payload = {"relative_path": "stone_library/raw.jpg", "rule": "stone_library"}

    response = client.post("/admin/file/image/process", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["rule"] == "stone_library"
    assert data["variants"] == []
