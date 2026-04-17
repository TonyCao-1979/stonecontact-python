from pydantic import BaseModel


class TrafficStatsListRequest(BaseModel):
    start_date: str | None = None
    end_date: str | None = None


class TrafficStatsItem(BaseModel):
    metric_name: str
    value: int | float


class TrafficStatsPage(BaseModel):
    items: list[TrafficStatsItem]
    total: int
