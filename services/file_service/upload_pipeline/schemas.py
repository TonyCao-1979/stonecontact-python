from pydantic import BaseModel


class UploadRequest(BaseModel):
    scheme: str
    file_name: str
    business_module: str | None = None


class BatchUploadRequest(BaseModel):
    files: list[UploadRequest]


class UploadItem(BaseModel):
    relative_path: str
    public_url: str | None = None


class BatchUploadResponse(BaseModel):
    items: list[UploadItem]
    total: int


class FileCopyRequest(BaseModel):
    source_path: str
    target: UploadRequest
