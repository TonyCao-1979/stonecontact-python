from pydantic import BaseModel


class JobLogItem(BaseModel):
    id: str
    job_id: str
    status: str
    message: str | None = None


class JobLogPage(BaseModel):
    items: list[JobLogItem]
    total: int


class RunNowResult(BaseModel):
    job_id: str
    status: str
