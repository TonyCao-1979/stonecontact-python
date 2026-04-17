from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class AuditEventEntry:
    id: str
    event_type: str
    actor: str | None = None
    detail: str | None = None
    created_at: datetime | None = None

