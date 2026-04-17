from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ErrorLogEntry:
    id: int
    system_name: str | None = None
    feature_type: str | None = None
    url: str | None = None
    http_code: str | None = None
    message: str | None = None
    created_at: datetime | None = None

