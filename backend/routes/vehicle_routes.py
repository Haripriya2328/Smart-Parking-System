from fastapi import APIRouter, HTTPException
from models import ParkingLog, VehicleExit, MessageResponse
from database import get_connection
from datetime import datetime

router = APIRouter()


# ================= VEHICLE ENTRY =================

@router.post("/parking/entry", response_model=MessageResponse)
def vehicle_entry(entry: ParkingLog):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Check whether the parking zone exists
        cursor.execute(
            """
            SELECT capacity, occupied_slots, available_slots
            FROM parking
            WHERE zone_id = %s
            """,
            (entry.parking_id,)
        )

        parking = cursor.fetchone()

        if parking is None:
            raise HTTPException(
                status_code=404,
                detail="Parking Zone Not Found"
            )

        capacity = parking[0]
        occupied_slots = parking[1]
        available_slots = parking[2]

        # Check whether parking is full
        if available_slots <= 0:
            raise HTTPException(
                status_code=400,
                detail="Parking is Full"
            )

        # Check whether the vehicle is already parked
        cursor.execute(
            """
            SELECT vehicle_id
            FROM parking_log
            WHERE vehicle_id = %s
            AND status = 'Parked'
            """,
            (entry.vehicle_id,)
        )

        vehicle = cursor.fetchone()

        if vehicle:
            raise HTTPException(
                status_code=400,
                detail="Vehicle is already parked"
            )

        # Store vehicle entry
        cursor.execute(
            """
            INSERT INTO parking_log (
                parking_id,
                vehicle_id,
                entry_time,
                exit_time,
                status
            )
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                entry.parking_id,
                entry.vehicle_id,
                entry.entry_time,
                entry.exit_time,
                entry.status
            )
        )

        # Update parking slot count
        cursor.execute(
            """
            UPDATE parking
            SET
                occupied_slots = occupied_slots + 1,
                available_slots = available_slots - 1
            WHERE zone_id = %s
            """,
            (entry.parking_id,)
        )

        connection.commit()

    except HTTPException:
        connection.rollback()
        raise

    except Exception as e:
        connection.rollback()

        print("ERROR:", e)

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        cursor.close()
        connection.close()

    return {
        "message": "Vehicle Entered Successfully"
    }


# ================= VEHICLE EXIT =================

@router.put("/parking/exit", response_model=MessageResponse)
def vehicle_exit(exit: VehicleExit):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Find the currently parked vehicle
        cursor.execute(
            """
            SELECT parking_id
            FROM parking_log
            WHERE vehicle_id = %s
            AND status = 'Parked'
            """,
            (exit.vehicle_id,)
        )

        parking = cursor.fetchone()

        if parking is None:
            raise HTTPException(
                status_code=404,
                detail="Vehicle is not currently parked"
            )

        parking_id = parking[0]

        # Update parking log
        cursor.execute(
            """
            UPDATE parking_log
            SET
                exit_time = %s,
                status = %s
            WHERE vehicle_id = %s
            AND status = 'Parked'
            """,
            (
                datetime.now(),
                "Exited",
                exit.vehicle_id
            )
        )

        # Update parking slot count
        cursor.execute(
            """
            UPDATE parking
            SET
                occupied_slots = occupied_slots - 1,
                available_slots = available_slots + 1
            WHERE zone_id = %s
            """,
            (parking_id,)
        )

        connection.commit()

    except HTTPException:
        connection.rollback()
        raise

    except Exception as e:
        connection.rollback()

        

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

    finally:
        cursor.close()
        connection.close()

    return {
        "message": "Vehicle Exited Successfully"
    }