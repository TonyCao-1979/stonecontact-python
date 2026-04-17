from fastapi import APIRouter

from domains.content.knowledge.schemas import KnowledgeTopicResponse
from domains.content.knowledge.service import KnowledgeService

router = APIRouter(prefix="/content/knowledge", tags=["content-site-knowledge"])

service = KnowledgeService()


@router.get("/by-stone-library/{stone_library_id}", response_model=list[KnowledgeTopicResponse])
def list_topics_by_stone_library(stone_library_id: int) -> list[KnowledgeTopicResponse]:
    return service.list_topics_by_stone_library(stone_library_id)
