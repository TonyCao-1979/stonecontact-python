from services.stats.stats_aggregation.schemas import AggregationStatusResponse


class StatsAggregationService:
    def get_status(self) -> AggregationStatusResponse:
        return AggregationStatusResponse(jobs=[])
