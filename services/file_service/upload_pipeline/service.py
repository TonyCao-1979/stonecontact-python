from services.file_service.upload_pipeline.schemas import (
    BatchUploadRequest,
    BatchUploadResponse,
    FileCopyRequest,
    UploadItem,
    UploadRequest,
)
from services.file_service.upload_validation.service import UploadValidationService


class UploadPipelineService:
    def __init__(self, validator: UploadValidationService | None = None) -> None:
        self.validator = validator or UploadValidationService()

    def upload_file(self, request: UploadRequest) -> UploadItem:
        self.validator.validate(request.file_name)
        return UploadItem(relative_path=f"{request.scheme}/{request.file_name}", public_url=None)

    def upload_batch(self, request: BatchUploadRequest) -> BatchUploadResponse:
        items = [self.upload_file(item) for item in request.files]
        return BatchUploadResponse(items=items, total=len(items))

    def copy_file(self, request: FileCopyRequest) -> UploadItem:
        self.validator.validate(request.target.file_name)
        return UploadItem(relative_path=f"{request.target.scheme}/{request.target.file_name}", public_url=None)
