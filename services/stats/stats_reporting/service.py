from services.stats.stats_reporting.schemas import StatsReportOverviewResponse


class StatsReportingService:
    def get_overview(self) -> StatsReportOverviewResponse:
        return StatsReportOverviewResponse(metrics=[])
