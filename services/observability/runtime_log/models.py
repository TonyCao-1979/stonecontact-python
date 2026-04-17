from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class RuntimeLogEntry:
    id: str
    event_type: str
    status: int | None = None
    detail: str | None = None
    created_at: datetime | None = None

