import logging
from config.datasource import db_session
from entity.charging_session import ChargingSession

logger = logging.getLogger(__name__)

async def create_charging_session(data):
    logger.info(f'Request to create new charging session: {data}')
    async with db_session().begin() as session:
        new_charging_session = ChargingSession(**data)
        session.add(new_charging_session)
        await session.commit()