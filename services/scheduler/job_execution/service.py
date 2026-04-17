from dataclasses import asdict

from services.scheduler.job_execution.repository import JobExecutionRepository
from services.scheduler.job_execution.schemas import JobLogItem, JobLogPage, RunNowResult


class JobExecutionService:
    def __init__(self, repository: JobExecutionRepository | None = None) -> None:
        self.repository = repository or JobExecutionRepository()

    def list_logs(self, job_id: str) -> JobLogPage:
        items = [JobLogItem.model_validate(asdict(entry)) for entry in self.repository.list_logs(job_id)]
        return JobLogPage(items=items, total=len(items))

    def run_now(self, job_id: str) -> RunNowResult:
        return RunNowResult(job_id=job_id, status="queued")
