from pydantic import BaseModel


class JobListRequest(BaseModel):
    keyword: str | None = None


class JobSaveRequest(BaseModel):
    id: str | None = None
    job_code: str
    name: str
    cron_expression: str | None = None
    is_enabled: bool = True


class JobItem(BaseModel):
    id: str
    job_code: str
    name: str
    cron_expression: str | None = None
    is_enabled: bool = True


class JobPage(BaseModel):
    items: list[JobItem]
    total: int
