from fastapi import APIRouter

from services.stats.traffic_stats.schemas import TrafficStatsListRequest, TrafficStatsPage
from services.stats.traffic_stats.service import TrafficStatsService

router = APIRouter(prefix="/admin/stats/traffic", tags=["stats-traffic"])

service = TrafficStatsService()


@router.post("/list", response_model=TrafficStatsPage)
def list_traffic_stats(request: TrafficStatsListRequest) -> TrafficStatsPage:
    return service.list_stats(request)
