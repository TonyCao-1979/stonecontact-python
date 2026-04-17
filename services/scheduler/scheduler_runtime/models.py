from dataclasses import dataclass


@dataclass(slots=True)
class SchedulerInstanceState:
    scheduler_name: str
    instance_name: str


@dataclass(slots=True)
class SchedulerTrigger:
    trigger_name: str
    trigger_group: str
    trigger_state: str
