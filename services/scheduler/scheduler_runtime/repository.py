from services.scheduler.scheduler_runtime.models import SchedulerInstanceState, SchedulerTrigger


class SchedulerRuntimeRepository:
    def list_instances(self) -> list[SchedulerInstanceState]:
        return []

    def list_triggers(self) -> list[SchedulerTrigger]:
        return []
