from fastapi import APIRouter, HTTPException

from services.scheduler.job_definition.schemas import JobListRequest, JobItem, JobPage, JobSaveRequest
from services.scheduler.job_definition.service import JobDefinitionService
from services.scheduler.job_execution.schemas import RunNowResult
from services.scheduler.job_execution.service import JobExecutionService

router = APIRouter(prefix="/admin/scheduler/jobs", tags=["scheduler-jobs"])

job_service = JobDefinitionService()
execution_service = JobExecutionService()


@router.post("/list", response_model=JobPage)
def list_jobs(request: JobListRequest) -> JobPage:
    return job_service.list_jobs(request)


@router.get("/{job_id}", response_model=JobItem)
def get_job(job_id: str) -> JobItem:
    job = job_service.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="job not found")
    return job


@router.post("/save", response_model=JobItem)
def save_job(request: JobSaveRequest) -> JobItem:
    return job_service.save_job(request)


@router.put("/{job_id}/enable", response_model=JobItem)
def enable_job(job_id: str) -> JobItem:
    return job_service.set_enabled(job_id, True)


@router.put("/{job_id}/disable", response_model=JobItem)
def disable_job(job_id: str) -> JobItem:
    return job_service.set_enabled(job_id, False)


@router.post("/{job_id}/run-now", response_model=RunNowResult)
def run_job_now(job_id: str) -> RunNowResult:
    return execution_service.run_now(job_id)
