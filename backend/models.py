from pydantic import BaseModel
from typing import Optional

class Parking(BaseModel):
  zone_id: int
  zone_name: str
  capacity: int
  occupied_slots: int
  available_slots: int
  latitude: float
  longitude: float
  directions:str
  
class ParkingLog(BaseModel):
  parking_id: int
  vehicle_id: str
  entry_time: str
  exit_time: Optional[str] = None
  status: str

class VehicleExit(BaseModel):
  vehicle_id: str
  

class MessageResponse(BaseModel):
  message: str