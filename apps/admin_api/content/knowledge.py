from fastapi import APIRouter

from domains.content.knowledge.schemas import KnowledgeItemUpdateRequest, KnowledgeItemUpdateResponse
from domains.content.knowledge.service import KnowledgeService

router = APIRouter(prefix="/admin/content/knowledge", tags=["content-admin-knowledge"])

service = KnowledgeService()


@router.post("/items/update", response_model=KnowledgeItemUpdateResponse)
def update_item(request: KnowledgeItemUpdateRequest) -> KnowledgeItemUpdateResponse:
    return service.update_item(request)
