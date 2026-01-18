from __future__ import annotations

from fastapi import FastAPI

from .routes import router as items_router

app = FastAPI(title="FastAPI Backend Example", version="1.0.0")
app.include_router(items_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
