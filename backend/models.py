from pydantic import BaseModel
class Parking(BaseModel):
  zone_id: int
  zone_name: str
  capacity: int
  occupied_slots: int
  available_slots: int
  