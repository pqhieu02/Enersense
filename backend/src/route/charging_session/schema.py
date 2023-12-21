from pydantic import BaseModel

class ChargingSession(BaseModel):
    id: int
    session_id: int
    energy_delivered_in_kWh: int
    duration_in_seconds: int
    session_cost_in_cents: int

    class Config:
        orm_mode = True