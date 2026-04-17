from pydantic import BaseModel


class AggregationJobItem(BaseModel):
    job_code: str
    status: str


class AggregationStatusResponse(BaseModel):
    jobs: list[AggregationJobItem]
