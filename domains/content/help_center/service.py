from dataclasses import asdict

from domains.content.help_center.repository import HelpCenterRepository
from domains.content.help_center.schemas import (
    HelpArticleUpdateRequest,
    HelpArticleUpdateResponse,
    HelpCategoryResponse,
)


class HelpCenterService:
    def __init__(self, repository: HelpCenterRepository | None = None) -> None:
        self.repository = repository or HelpCenterRepository()

    def list_categories(self) -> list[HelpCategoryResponse]:
        return [
            HelpCategoryResponse.model_validate(asdict(category))
            for category in self.repository.list_categories()
        ]

    def update_article(self, request: HelpArticleUpdateRequest) -> HelpArticleUpdateResponse:
        return HelpArticleUpdateResponse(ok=True, article_id=request.article_id)
