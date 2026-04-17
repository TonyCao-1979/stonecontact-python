from fastapi import FastAPI

from apps.site_api.content.help_center import router as content_help_center_router
from apps.site_api.content.knowledge import router as content_knowledge_router

app = FastAPI(title="stonecontact site api")

app.include_router(content_knowledge_router)
app.include_router(content_help_center_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "app": "site_api"}
