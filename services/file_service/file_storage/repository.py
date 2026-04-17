from services.file_service.file_storage.models import StoredFile


class FileStorageRepository:
    def get_file(self, relative_path: str) -> StoredFile:
        return StoredFile(relative_path=relative_path)
