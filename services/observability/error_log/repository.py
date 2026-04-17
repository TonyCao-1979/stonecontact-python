from services.observability.error_log.models import ErrorLogEntry


class ErrorLogRepository:
    """Placeholder repository for future StoneContactLog.Log_Error mapping."""

    def list_entries(self) -> list[ErrorLogEntry]:
        return []

    def get_entry(self, entry_id: int) -> ErrorLogEntry | None:
        return None

