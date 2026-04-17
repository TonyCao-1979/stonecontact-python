from fastapi import APIRouter

from services.stats.stats_reporting.schemas import StatsReportOverviewResponse
from services.stats.stats_reporting.service import StatsReportingService

router = APIRouter(prefix="/admin/stats/reports", tags=["stats-reports"])

service = StatsReportingService()


@router.get("/overview", response_model=StatsReportOverviewResponse)
def get_report_overview() -> StatsReportOverviewResponse:
    return service.get_overview()
