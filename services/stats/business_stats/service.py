from services.stats.business_stats.schemas import BusinessStatsListRequest, BusinessStatsPage


class BusinessStatsService:
    def list_stats(self, _: BusinessStatsListRequest) -> BusinessStatsPage:
        return BusinessStatsPage(items=[], total=0)
