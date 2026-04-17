from pydantic import BaseModel


class KnowledgeTopicResponse(BaseModel):
    id: str
    title: str
    stone_library_id: int | None


class KnowledgeItemUpdateRequest(BaseModel):
    item_id: int
    title: str
    content: str


class KnowledgeItemUpdateResponse(BaseModel):
    ok: bool
    item_id: int
