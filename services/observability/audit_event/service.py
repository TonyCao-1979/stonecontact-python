from services.observability.audit_event.repository import AuditEventRepository
from services.observability.audit_event.schemas import AuditEventItem, AuditEventListRequest, AuditEventPage


class AuditEventService:
    def __init__(self, repository: AuditEventRepository | None = None) -> None:
        self.repository = repository or AuditEventRepository()

    def list_events(self, _: AuditEventListRequest) -> AuditEventPage:
        items = [AuditEventItem.model_validate(entry.__dict__) for entry in self.repository.list_events()]
        return AuditEventPage(items=items, total=len(items))

