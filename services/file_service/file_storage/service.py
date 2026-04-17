from dataclasses import asdict

from services.file_service.file_storage.repository import FileStorageRepository
from services.file_service.file_storage.schemas import FileDeleteResponse, FileDownloadResponse


class FileStorageService:
    def __init__(self, repository: FileStorageRepository | None = None) -> None:
        self.repository = repository or FileStorageRepository()

    def get_file(self, relative_path: str) -> FileDownloadResponse:
        return FileDownloadResponse.model_validate(asdict(self.repository.get_file(relative_path)))

    def delete_file(self, relative_path: str) -> FileDeleteResponse:
        return FileDeleteResponse(relative_path=relative_path, deleted=True)
