from sqlalchemy import Column, Integer

from src.config.datasource import Base

class ChargingSession(Base):
    __tablename__ = "charging_session"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer)
    energy_delivered_in_kWh = Column(Integer)
    duration_in_seconds = Column(Integer)
    session_cost_in_cents = Column(Integer)
