from fastapi import APIRouter, HTTPException
from models import Parking
from database import get_connection
router=APIRouter()

@router.get("/")
def home():
    return {
        "message":"Welcome to Smart Parking System"
    }

#==========GET ALL PARKING ==========

@router.get("/parking",response_model=list[Parking])
def get_parking():
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute("""SELECT *
                   FROM parking 
                   ORDER BY zone_id
                   """)
    parking=cursor.fetchall()
    result=[]
    for row in parking:
        parking_dict = {
            "zone_id": row[0],
            "zone_name": row[1],
            "capacity": row[2],
            "occupied_slots": row[3],
            "available_slots": row[4]
        }

        result.append(parking_dict)

    cursor.close()
    connection.close()

    return result
    
#==========SEARCH BY NAME=========

@router.get("/parking/search",response_model=Parking)
def search_parking(name: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM parking
        WHERE LOWER(zone_name) = LOWER(%s)
        """,
        (name,)
    )

    parking = cursor.fetchone()
    cursor.close()
    connection.close()
    if parking:
        return {
            "zone_id": parking[0],
            "zone_name": parking[1],
            "capacity": parking[2],
            "occupied_slots": parking[3],
            "available_slots": parking[4]
        }
    raise HTTPException(
    status_code=404,
    detail="Parking Zone Not Found"
    )

#=======GET BY ID============
 
@router.get("/parking/{zone_id}",response_model=Parking)
def get_parking_by_id(zone_id: int):

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM parking
        WHERE zone_id = %s
        """,
        (zone_id,)
    )

    parking = cursor.fetchone()
    cursor.close()
    connection.close()
    if parking:
         return {
            "zone_id": parking[0],
            "zone_name": parking[1],
            "capacity": parking[2],
            "occupied_slots": parking[3],
            "available_slots": parking[4]
        }
    raise HTTPException(
    status_code=404,
    detail="Parking Zone Not Found"
    )

#========ADD PARKING=========

@router.post("/parking")
def add_parking(parking: Parking):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO parking
        (zone_id, zone_name, capacity, occupied_slots, available_slots)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            parking.zone_id,
            parking.zone_name,
            parking.capacity,
            parking.occupied_slots,
            parking.available_slots
        )
    )

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Parking Zone Added Successfully"
    }

#=========UPDATE PARKING==========

@router.put("/parking/{zone_id}")
def update_parking(zone_id: int, parking: Parking):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE parking
        SET
            zone_name = %s,
            capacity = %s,
            occupied_slots = %s,
            available_slots = %s
        WHERE zone_id = %s
        """,
        (
            parking.zone_name,
            parking.capacity,
            parking.occupied_slots,
            parking.available_slots,
            zone_id
        )
    )
    if cursor.rowcount == 0:

        cursor.close()
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Parking Zone Not Found"
        )

    connection.commit()
    cursor.close()
    connection.close()

    return {
        "message": "Parking Updated Successfully"
    }

#==========DELETE PARKING==========    
    
@router.delete("/parking/{zone_id}")
def delete_parking(zone_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        DELETE FROM parking
        WHERE zone_id = %s
        """,
        (zone_id,)
    )
    if cursor.rowcount == 0:

        cursor.close()
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Parking Zone Not Found"
        )

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Parking Zone Deleted Successfully"
    }
