from pydantic import BaseModel


class BusinessStatsListRequest(BaseModel):
    start_date: str | None = None
    end_date: str | None = None


class BusinessStatsItem(BaseModel):
    metric_name: str
    value: int | float


class BusinessStatsPage(BaseModel):
    items: list[BusinessStatsItem]
    total: int
