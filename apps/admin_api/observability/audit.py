from fastapi import APIRouter

from services.observability.audit_event.schemas import AuditEventListRequest
from services.observability.audit_event.service import AuditEventService

router = APIRouter(prefix="/admin/observability/audit", tags=["observability-audit"])
service = AuditEventService()


@router.post("/list")
def list_audit_events(request: AuditEventListRequest):
    return service.list_events(request)

