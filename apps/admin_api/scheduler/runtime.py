from fastapi import APIRouter

from services.scheduler.scheduler_runtime.schemas import SchedulerStateResponse, SchedulerTriggerPage
from services.scheduler.scheduler_runtime.service import SchedulerRuntimeService

router = APIRouter(prefix="/admin/scheduler/runtime", tags=["scheduler-runtime"])

service = SchedulerRuntimeService()


@router.get("/state", response_model=SchedulerStateResponse)
def get_state() -> SchedulerStateResponse:
    return service.get_state()


@router.get("/triggers", response_model=SchedulerTriggerPage)
def list_triggers() -> SchedulerTriggerPage:
    return service.list_triggers()
