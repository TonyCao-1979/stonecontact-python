from datetime import datetime

from pydantic import BaseModel


class RuntimeLogListRequest(BaseModel):
    event_type: str | None = None
    page: int = 1
    page_size: int = 20


class RuntimeLogItem(BaseModel):
    id: str
    event_type: str
    status: int | None = None
    detail: str | None = None
    created_at: datetime | None = None


class RuntimeLogPage(BaseModel):
    items: list[RuntimeLogItem]
    total: int

