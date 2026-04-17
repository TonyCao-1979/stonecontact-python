from fastapi import APIRouter

from services.observability.runtime_log.schemas import RuntimeLogListRequest
from services.observability.runtime_log.service import RuntimeLogService

router = APIRouter(prefix="/admin/observability/runtime", tags=["observability-runtime"])
service = RuntimeLogService()


@router.post("/list")
def list_runtime_logs(request: RuntimeLogListRequest):
    return service.list_logs(request)

