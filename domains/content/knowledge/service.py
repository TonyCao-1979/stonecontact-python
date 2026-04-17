from dataclasses import asdict

from domains.content.knowledge.repository import KnowledgeRepository
from domains.content.knowledge.schemas import (
    KnowledgeItemUpdateRequest,
    KnowledgeItemUpdateResponse,
    KnowledgeTopicResponse,
)


class KnowledgeService:
    def __init__(self, repository: KnowledgeRepository | None = None) -> None:
        self.repository = repository or KnowledgeRepository()

    def list_topics_by_stone_library(self, stone_library_id: int) -> list[KnowledgeTopicResponse]:
        return [
            KnowledgeTopicResponse.model_validate(asdict(topic))
            for topic in self.repository.get_topics_by_stone_library(stone_library_id)
        ]

    def update_item(self, request: KnowledgeItemUpdateRequest) -> KnowledgeItemUpdateResponse:
        return KnowledgeItemUpdateResponse(ok=True, item_id=request.item_id)
