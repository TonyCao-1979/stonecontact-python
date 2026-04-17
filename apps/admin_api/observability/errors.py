from fastapi import APIRouter, HTTPException

from services.observability.error_log.schemas import ErrorLogListRequest
from services.observability.error_log.service import ErrorLogService

router = APIRouter(prefix="/admin/observability/errors", tags=["observability-errors"])
service = ErrorLogService()


@router.post("/list")
def list_error_logs(request: ErrorLogListRequest):
    return service.list_logs(request)


@router.get("/{entry_id}")
def get_error_log(entry_id: int):
    item = service.get_log(entry_id)
    if item is None:
        raise HTTPException(status_code=404, detail="error log not found")
    return item

