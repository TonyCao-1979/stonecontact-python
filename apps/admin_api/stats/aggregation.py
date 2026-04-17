from fastapi import APIRouter

from services.stats.stats_aggregation.schemas import AggregationStatusResponse
from services.stats.stats_aggregation.service import StatsAggregationService

router = APIRouter(prefix="/admin/stats/aggregation", tags=["stats-aggregation"])

service = StatsAggregationService()


@router.get("/status", response_model=AggregationStatusResponse)
def get_aggregation_status() -> AggregationStatusResponse:
    return service.get_status()
