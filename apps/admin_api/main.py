from fastapi import FastAPI

from apps.admin_api.observability.audit import router as audit_router
from apps.admin_api.observability.errors import router as error_router
from apps.admin_api.observability.monitors import router as monitor_router
from apps.admin_api.observability.runtime import router as runtime_router

app = FastAPI(title="stonecontact admin api")

app.include_router(error_router)
app.include_router(runtime_router)
app.include_router(monitor_router)
app.include_router(audit_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "app": "admin_api"}
