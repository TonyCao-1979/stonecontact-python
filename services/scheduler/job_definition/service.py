from dataclasses import asdict
from uuid import uuid4

from services.scheduler.job_definition.models import JobDefinition
from services.scheduler.job_definition.repository import JobDefinitionRepository
from services.scheduler.job_definition.schemas import JobItem, JobListRequest, JobPage, JobSaveRequest


class JobDefinitionService:
    def __init__(self, repository: JobDefinitionRepository | None = None) -> None:
        self.repository = repository or JobDefinitionRepository()

    def list_jobs(self, _: JobListRequest) -> JobPage:
        items = [JobItem.model_validate(asdict(entry)) for entry in self.repository.list_jobs()]
        return JobPage(items=items, total=len(items))

    def get_job(self, job_id: str) -> JobItem | None:
        entry = self.repository.get_job(job_id)
        if entry is None:
            return None
        return JobItem.model_validate(asdict(entry))

    def save_job(self, request: JobSaveRequest) -> JobItem:
        entry = JobDefinition(
            id=request.id or str(uuid4()),
            job_code=request.job_code,
            name=request.name,
            cron_expression=request.cron_expression,
            is_enabled=request.is_enabled,
        )
        return JobItem.model_validate(asdict(entry))

    def set_enabled(self, job_id: str, is_enabled: bool) -> JobItem:
        entry = JobDefinition(
            id=job_id,
            job_code=f"job_{job_id}",
            name=f"Job {job_id}",
            is_enabled=is_enabled,
        )
        return JobItem.model_validate(asdict(entry))
