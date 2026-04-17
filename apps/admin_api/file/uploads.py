from fastapi import APIRouter

from services.file_service.image_processing.schemas import ImageProcessRequest, ImageProcessResponse
from services.file_service.image_processing.service import ImageProcessingService
from services.file_service.upload_pipeline.schemas import (
    BatchUploadRequest,
    BatchUploadResponse,
    FileCopyRequest,
    UploadItem,
    UploadRequest,
)
from services.file_service.upload_pipeline.service import UploadPipelineService

router = APIRouter(prefix="/admin/file", tags=["file-uploads"])

upload_service = UploadPipelineService()
image_service = ImageProcessingService()


@router.post("/upload", response_model=UploadItem)
def upload_file(request: UploadRequest) -> UploadItem:
    return upload_service.upload_file(request)


@router.post("/upload/batch", response_model=BatchUploadResponse)
def upload_batch(request: BatchUploadRequest) -> BatchUploadResponse:
    return upload_service.upload_batch(request)


@router.post("/copy", response_model=UploadItem)
def copy_file(request: FileCopyRequest) -> UploadItem:
    return upload_service.copy_file(request)


@router.post("/image/process", response_model=ImageProcessResponse)
def process_image(request: ImageProcessRequest) -> ImageProcessResponse:
    return image_service.process(request)
