import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config.datasource import create_tables, db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # On start up event
    await create_tables()
    yield 
    # On shutdown event
    # Use asyncio.shield to ensure that the database connection is closed before shutting down
    await asyncio.shield(db.dispose())

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"message": "ok"}

from src.route.charging_session.router import router as charging_session_router
app.include_router(charging_session_router, prefix="/api/charging-session")