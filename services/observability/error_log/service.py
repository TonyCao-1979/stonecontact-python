from services.observability.error_log.repository import ErrorLogRepository
from services.observability.error_log.schemas import ErrorLogItem, ErrorLogListRequest, ErrorLogPage


class ErrorLogService:
    def __init__(self, repository: ErrorLogRepository | None = None) -> None:
        self.repository = repository or ErrorLogRepository()

    def list_logs(self, _: ErrorLogListRequest) -> ErrorLogPage:
        items = [ErrorLogItem.model_validate(entry.__dict__) for entry in self.repository.list_entries()]
        return ErrorLogPage(items=items, total=len(items))

    def get_log(self, entry_id: int) -> ErrorLogItem | None:
        entry = self.repository.get_entry(entry_id)
        if entry is None:
            return None
        return ErrorLogItem.model_validate(entry.__dict__)

