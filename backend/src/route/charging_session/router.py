import logging
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from src.config.datasource import Session, get_db
from src.entity.charging_session import ChargingSession
from . import schema

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/', response_model=List[schema.ChargingSession])
async def get_all_charging_sessions(db: Session = Depends(get_db)):
    res = await db.execute(select(ChargingSession))
    return res.scalars().all()
