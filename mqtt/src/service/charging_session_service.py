import logging
from config.datasource import Session
from entity.charging_session import ChargingSession

logger = logging.getLogger(__name__)

def create_charging_session(data):
    logger.info(f'Request to create new charging session: {data}')
    with Session.begin() as session:
        new_charging_session = ChargingSession(**data)
        session.add(new_charging_session)
        session.commit()