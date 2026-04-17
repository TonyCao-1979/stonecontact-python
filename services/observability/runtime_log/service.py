from services.observability.runtime_log.repository import RuntimeLogRepository
from services.observability.runtime_log.schemas import RuntimeLogItem, RuntimeLogListRequest, RuntimeLogPage


class RuntimeLogService:
    def __init__(self, repository: RuntimeLogRepository | None = None) -> None:
        self.repository = repository or RuntimeLogRepository()

    def list_logs(self, _: RuntimeLogListRequest) -> RuntimeLogPage:
        items = [RuntimeLogItem.model_validate(entry.__dict__) for entry in self.repository.list_entries()]
        return RuntimeLogPage(items=items, total=len(items))

