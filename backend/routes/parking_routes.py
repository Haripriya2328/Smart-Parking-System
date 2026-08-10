from fastapi import APIRouter, HTTPException
from models import Parking, MessageResponse
from database import get_connection
import math

router = APIRouter()
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
            "available_slots": row[4],
            "latitude": row[5],
            "longitude": row[6],
            "directions": row[7]
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
            "available_slots": parking[4],
            "latitude": parking[5],
            "longitude": parking[6],
            "directions": parking[7]

        }
    raise HTTPException(
    status_code=404,
    detail="Parking Zone Not Found"
    )

@router.get("/parking/nearest")
def nearest_parking(latitude: float, longitude: float):

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT *
        FROM parking
        """
    )
    parking_zones = cursor.fetchall()
    result = []
    for row in parking_zones:
        parking_lat = float(row[5])
        parking_lon = float(row[6])

        distance=math.sqrt(
            (latitude-parking_lat)**2 + (longitude-parking_lon)**2
        )

        result.append({
            "zone_id": row[0],
            "zone_name": row[1],
            "capacity": row[2],
            "occupied_slots": row[3],
            "available_slots": row[4],
            "latitude": row[5],
            "longitude": row[6],
            "distance": distance
        })
    result.sort(key=lambda x: x["distance"])
    cursor.close()
    connection.close()
    if len(result) == 0:
        raise HTTPException(
            status_code=404,
            detail="No Parking Zones Found"
        )
    return result[0] 
    

#=======GET BY ID============
 
@router.get("/parking/id/{zone_id}",response_model=Parking)
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
            "available_slots": parking[4],
            "latitude": parking[5],
            "longitude": parking[6],
            "directions": parking[7]
        }
    raise HTTPException(
    status_code=404,
    detail="Parking Zone Not Found"
    )


#========ADD PARKING=========
@router.post("/parking", response_model=MessageResponse)
def add_parking(parking: Parking):

    
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO parking
            (zone_id, zone_name, capacity, occupied_slots, available_slots, latitude, longitude,directions)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                parking.zone_id,
                parking.zone_name,
                parking.capacity,
                parking.occupied_slots,
                parking.available_slots,
                parking.latitude,
                parking.longitude,
                parking.directions
            )
        )

        connection.commit()

        cursor.close()
        connection.close()

        return {
            "message": "Parking Zone Added Successfully"
        }

    

#=========UPDATE PARKING==========

@router.put("/parking/update/{zone_id}", response_model=MessageResponse)
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
            available_slots = %s,
            latitude = %s,
            longitude = %s,
            directions=%s
        WHERE zone_id = %s
        """,
        (
            parking.zone_name,
            parking.capacity,
            parking.occupied_slots,
            parking.available_slots,
            parking.latitude,
            parking.longitude,
            parking.directions,
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
@router.delete("/parking/{zone_id}", response_model=MessageResponse)
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
