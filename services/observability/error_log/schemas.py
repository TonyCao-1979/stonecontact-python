from datetime import datetime

from pydantic import BaseModel


class ErrorLogListRequest(BaseModel):
    keyword: str | None = None
    page: int = 1
    page_size: int = 20


class ErrorLogItem(BaseModel):
    id: int
    system_name: str | None = None
    feature_type: str | None = None
    url: str | None = None
    http_code: str | None = None
    message: str | None = None
    created_at: datetime | None = None


class ErrorLogPage(BaseModel):
    items: list[ErrorLogItem]
    total: int

