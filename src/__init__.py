from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.rest.router import charging_session_router
from src.config.datasource import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # On start up event
    yield 
    # On shutdown event
    db.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"message": "ok"}

app.include_router(charging_session_router.router, prefix="/api/charging-session")