from dataclasses import dataclass


@dataclass(slots=True)
class KnowledgeTopic:
    id: str
    title: str
    stone_library_id: int | None


@dataclass(slots=True)
class KnowledgeItem:
    id: int
    title: str
    content: str
