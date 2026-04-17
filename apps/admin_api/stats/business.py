from fastapi import APIRouter

from services.stats.business_stats.schemas import BusinessStatsListRequest, BusinessStatsPage
from services.stats.business_stats.service import BusinessStatsService

router = APIRouter(prefix="/admin/stats/business", tags=["stats-business"])

service = BusinessStatsService()


@router.post("/list", response_model=BusinessStatsPage)
def list_business_stats(request: BusinessStatsListRequest) -> BusinessStatsPage:
    return service.list_stats(request)
