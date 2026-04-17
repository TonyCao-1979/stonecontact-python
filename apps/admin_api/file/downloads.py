from fastapi import APIRouter

from services.file_service.file_storage.schemas import FileDeleteRequest, FileDeleteResponse, FileDownloadResponse
from services.file_service.file_storage.service import FileStorageService

router = APIRouter(prefix="/admin/file", tags=["file-downloads"])

service = FileStorageService()


@router.get("/download", response_model=FileDownloadResponse)
def download_file(relative_path: str) -> FileDownloadResponse:
    return service.get_file(relative_path)


@router.delete("", response_model=FileDeleteResponse)
def delete_file(request: FileDeleteRequest) -> FileDeleteResponse:
    return service.delete_file(request.relative_path)
