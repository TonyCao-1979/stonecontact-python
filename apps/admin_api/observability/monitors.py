from fastapi import APIRouter

from services.observability.system_monitor.schemas import MonitorListRequest, MonitorSaveRequest
from services.observability.system_monitor.service import SystemMonitorService

router = APIRouter(prefix="/admin/observability/monitors", tags=["observability-monitors"])
service = SystemMonitorService()


@router.post("/list")
def list_monitors(request: MonitorListRequest):
    return service.list_monitors(request)


@router.post("/save")
def save_monitor(request: MonitorSaveRequest):
    return service.save_monitor(request)

