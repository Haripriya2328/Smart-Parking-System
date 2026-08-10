from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.parking_routes import router as parking_router
from routes.vehicle_routes import router as vehicle_router
from routes.dashboard_routes import router as dashboard_router
from routes.history_routes import router as history_router
app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(parking_router)
app.include_router(vehicle_router)
app.include_router(dashboard_router)
app.include_router(history_router)