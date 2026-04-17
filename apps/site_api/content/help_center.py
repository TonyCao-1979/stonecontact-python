from fastapi import APIRouter

from domains.content.help_center.schemas import HelpCategoryResponse
from domains.content.help_center.service import HelpCenterService

router = APIRouter(prefix="/content/help-center", tags=["content-site-help-center"])

service = HelpCenterService()


@router.get("/categories", response_model=list[HelpCategoryResponse])
def list_categories() -> list[HelpCategoryResponse]:
    return service.list_categories()
