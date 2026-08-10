from fastapi import APIRouter
from database import get_connection

router = APIRouter()


# ================= ALL PARKING HISTORY =================

@router.get("/parking/history")
def parking_history():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            SELECT *
            FROM parking_log
            ORDER BY log_id
            """
        )

        history = cursor.fetchall()

        result = []

        for row in history:

            result.append(
                {
                    "log_id": row[0],
                    "parking_id": row[1],
                    "vehicle_id": row[2],
                    "entry_time": row[3],
                    "exit_time": row[4],
                    "status": row[5]
                }
            )

        return result

    finally:
        cursor.close()
        connection.close()


# ================= VEHICLE HISTORY =================

@router.get("/parking/history/{vehicle_id}")
def get_vehicle_history(vehicle_id: str):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            SELECT *
            FROM parking_log
            WHERE vehicle_id = %s
            ORDER BY log_id
            """,
            (vehicle_id,)
        )

        history = cursor.fetchall()

        result = []

        for row in history:

            result.append(
                {
                    "log_id": row[0],
                    "parking_id": row[1],
                    "vehicle_id": row[2],
                    "entry_time": row[3],
                    "exit_time": row[4],
                    "status": row[5]
                }
            )

        return result

    finally:
        cursor.close()
        connection.close()