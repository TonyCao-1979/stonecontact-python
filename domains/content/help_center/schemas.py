from pydantic import BaseModel


class HelpCategoryResponse(BaseModel):
    id: int
    name: str
    is_enabled: bool


class HelpArticleUpdateRequest(BaseModel):
    article_id: int
    title: str
    content: str


class HelpArticleUpdateResponse(BaseModel):
    ok: bool
    article_id: int
