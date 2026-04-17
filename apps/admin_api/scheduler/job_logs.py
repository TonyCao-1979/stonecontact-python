from fastapi import APIRouter

from services.scheduler.job_execution.schemas import JobLogPage
from services.scheduler.job_execution.service import JobExecutionService

router = APIRouter(prefix="/admin/scheduler/jobs", tags=["scheduler-job-logs"])

service = JobExecutionService()


@router.get("/{job_id}/logs", response_model=JobLogPage)
def list_job_logs(job_id: str) -> JobLogPage:
    return service.list_logs(job_id)
