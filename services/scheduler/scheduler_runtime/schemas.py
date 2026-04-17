from pydantic import BaseModel


class SchedulerInstanceItem(BaseModel):
    scheduler_name: str
    instance_name: str


class SchedulerStateResponse(BaseModel):
    instances: list[SchedulerInstanceItem]


class SchedulerTriggerItem(BaseModel):
    trigger_name: str
    trigger_group: str
    trigger_state: str


class SchedulerTriggerPage(BaseModel):
    items: list[SchedulerTriggerItem]
    total: int
