from datetime import datetime

from pydantic import BaseModel


class AuditEventListRequest(BaseModel):
    event_type: str | None = None
    page: int = 1
    page_size: int = 20


class AuditEventItem(BaseModel):
    id: str
    event_type: str
    actor: str | None = None
    detail: str | None = None
    created_at: datetime | None = None


class AuditEventPage(BaseModel):
    items: list[AuditEventItem]
    total: int

