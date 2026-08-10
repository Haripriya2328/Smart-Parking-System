from fastapi import APIRouter
from database import get_connection

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Total Parking Zones
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM parking
            """
        )
        total_parking_zones = cursor.fetchone()[0]

        # Total Parking Capacity
        cursor.execute(
            """
            SELECT SUM(capacity)
            FROM parking
            """
        )
        total_capacity = cursor.fetchone()[0]

        # Total Occupied Slots
        cursor.execute(
            """
            SELECT SUM(occupied_slots)
            FROM parking
            """
        )
        total_occupied = cursor.fetchone()[0]

        # Total Available Slots
        cursor.execute(
            """
            SELECT SUM(available_slots)
            FROM parking
            """
        )
        total_available = cursor.fetchone()[0]

        # Vehicles Currently Parked
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM parking_log
            WHERE status = 'Parked'
            """
        )
        vehicles_currently_parked = cursor.fetchone()[0]

        return {
            "total_parking_zones": total_parking_zones,
            "total_capacity": total_capacity,
            "total_occupied": total_occupied,
            "total_available": total_available,
            "vehicles_currently_parked": vehicles_currently_parked
        }

    finally:
        cursor.close()
        connection.close()