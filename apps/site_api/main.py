from fastapi import FastAPI

app = FastAPI(title="stonecontact site api")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "app": "site_api"}

