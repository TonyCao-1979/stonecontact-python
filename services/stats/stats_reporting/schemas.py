from pydantic import BaseModel


class ReportMetricItem(BaseModel):
    metric_name: str
    value: int | float


class StatsReportOverviewResponse(BaseModel):
    metrics: list[ReportMetricItem]
