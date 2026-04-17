from fastapi import FastAPI

from apps.admin_api.file.downloads import router as file_downloads_router
from apps.admin_api.file.uploads import router as file_uploads_router
from apps.admin_api.observability.audit import router as audit_router
from apps.admin_api.observability.errors import router as error_router
from apps.admin_api.observability.monitors import router as monitor_router
from apps.admin_api.observability.runtime import router as runtime_router
from apps.admin_api.scheduler.job_logs import router as scheduler_job_logs_router
from apps.admin_api.scheduler.jobs import router as scheduler_jobs_router
from apps.admin_api.scheduler.runtime import router as scheduler_runtime_router

app = FastAPI(title="stonecontact admin api")

app.include_router(error_router)
app.include_router(runtime_router)
app.include_router(monitor_router)
app.include_router(audit_router)
app.include_router(file_uploads_router)
app.include_router(file_downloads_router)
app.include_router(scheduler_jobs_router)
app.include_router(scheduler_job_logs_router)
app.include_router(scheduler_runtime_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "app": "admin_api"}
