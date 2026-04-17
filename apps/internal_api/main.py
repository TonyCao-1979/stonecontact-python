from fastapi import FastAPI

app = FastAPI(title="stonecontact internal api")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "app": "internal_api"}

