from dataclasses import asdict

from services.scheduler.scheduler_runtime.repository import SchedulerRuntimeRepository
from services.scheduler.scheduler_runtime.schemas import (
    SchedulerInstanceItem,
    SchedulerStateResponse,
    SchedulerTriggerItem,
    SchedulerTriggerPage,
)


class SchedulerRuntimeService:
    def __init__(self, repository: SchedulerRuntimeRepository | None = None) -> None:
        self.repository = repository or SchedulerRuntimeRepository()

    def get_state(self) -> SchedulerStateResponse:
        items = [SchedulerInstanceItem.model_validate(asdict(entry)) for entry in self.repository.list_instances()]
        return SchedulerStateResponse(instances=items)

    def list_triggers(self) -> SchedulerTriggerPage:
        items = [SchedulerTriggerItem.model_validate(asdict(entry)) for entry in self.repository.list_triggers()]
        return SchedulerTriggerPage(items=items, total=len(items))
