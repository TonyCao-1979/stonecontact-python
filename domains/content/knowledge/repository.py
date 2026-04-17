from domains.content.knowledge.models import KnowledgeTopic


class KnowledgeRepository:
    def get_topics_by_stone_library(self, stone_library_id: int) -> list[KnowledgeTopic]:
        return [KnowledgeTopic(id="k1", title="Granite Guide", stone_library_id=stone_library_id)]
