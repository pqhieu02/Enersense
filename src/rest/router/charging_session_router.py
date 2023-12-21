import logging
from fastapi import APIRouter
from src.config.datasource import Session

from src.entity.charging_session import ChargingSession

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get('/')
def get_all_charging_sessions():
    result: list[ChargingSession] = []
    with Session() as session:
        result = session.query(ChargingSession).all()
    return {'status': 'OK', 'data': result}