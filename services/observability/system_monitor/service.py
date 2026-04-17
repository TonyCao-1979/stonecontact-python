from dataclasses import asdict
from uuid import uuid4

from services.observability.system_monitor.models import MonitorDefinition
from services.observability.system_monitor.repository import SystemMonitorRepository
from services.observability.system_monitor.schemas import MonitorItem, MonitorListRequest, MonitorPage, MonitorSaveRequest


class SystemMonitorService:
    def __init__(self, repository: SystemMonitorRepository | None = None) -> None:
        self.repository = repository or SystemMonitorRepository()

    def list_monitors(self, _: MonitorListRequest) -> MonitorPage:
        items = [MonitorItem.model_validate(asdict(entry)) for entry in self.repository.list_monitors()]
        return MonitorPage(items=items, total=len(items))

    def save_monitor(self, request: MonitorSaveRequest) -> MonitorItem:
        entry = MonitorDefinition(
            id=request.id or str(uuid4()),
            system_name=request.system_name,
            monitor_type=request.monitor_type,
            is_enabled=request.is_enabled,
        )
        return MonitorItem.model_validate(asdict(entry))
