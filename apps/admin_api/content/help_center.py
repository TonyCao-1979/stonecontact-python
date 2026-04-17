from fastapi import APIRouter

from domains.content.help_center.schemas import HelpArticleUpdateRequest, HelpArticleUpdateResponse
from domains.content.help_center.service import HelpCenterService

router = APIRouter(prefix="/admin/content/help-center", tags=["content-admin-help-center"])

service = HelpCenterService()


@router.post("/articles/update", response_model=HelpArticleUpdateResponse)
def update_article(request: HelpArticleUpdateRequest) -> HelpArticleUpdateResponse:
    return service.update_article(request)
