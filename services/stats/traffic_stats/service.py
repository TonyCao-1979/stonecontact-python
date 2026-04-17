from services.stats.traffic_stats.schemas import TrafficStatsListRequest, TrafficStatsPage


class TrafficStatsService:
    def list_stats(self, _: TrafficStatsListRequest) -> TrafficStatsPage:
        return TrafficStatsPage(items=[], total=0)
