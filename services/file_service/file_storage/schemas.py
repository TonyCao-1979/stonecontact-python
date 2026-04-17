from pydantic import BaseModel


class FileDownloadResponse(BaseModel):
    relative_path: str
    content_type: str | None = None
    size: int | None = None


class FileDeleteRequest(BaseModel):
    relative_path: str


class FileDeleteResponse(BaseModel):
    relative_path: str
    deleted: bool
