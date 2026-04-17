from fastapi import FastAPI

app = FastAPI(title="stonecontact admin api")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "app": "admin_api"}

