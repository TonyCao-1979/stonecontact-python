from dataclasses import dataclass


@dataclass(slots=True)
class JobExecutionLog:
    id: str
    job_id: str
    status: str
    message: str | None = None
