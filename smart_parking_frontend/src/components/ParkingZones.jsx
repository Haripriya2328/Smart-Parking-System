import { useEffect, useState } from "react";

function ParkingZones() {

    const [parkingZones, setParkingZones] = useState([]);
    const [selectedParking, setSelectedParking] = useState(null);
    const [showDirections, setShowDirections] = useState(false);

    useEffect(() => {
        fetchParkingZones();
    }, []);

    async function fetchParkingZones() {
        try {
            const response = await fetch("http://127.0.0.1:8000/parking");
            if (!response.ok){
                throw new Error("Failed to fetch parking zones");
            }
            const data = await response.json();
            setParkingZones(data);
        } catch (error) {
            console.log("Error:", error);
        }
    }

    function handleNavigate(parking) {
        setSelectedParking(parking);
        setShowDirections(true);
    }

    return (
        <section id="parking-zones">

            <h2>📍 Available Parking Zones</h2>

            <table className="parking-table">

                <thead>
                    <tr>
                        <th>Zone ID</th>
                        <th>Parking Zone</th>
                        <th>Capacity</th>
                        <th>Occupied</th>
                        <th>Available</th>
                        <th>Status</th>
                        <th>Navigate</th>
                    </tr>
                </thead>

                <tbody>
                    {parkingZones.map((parking) => (
                        <tr key={parking.zone_id}>

                            <td>{parking.zone_id}</td>

                            <td>{parking.zone_name}</td>

                            <td>{parking.capacity}</td>

                            <td>{parking.occupied_slots}</td>

                            <td
                                style={{
                                    color:
                                        parking.available_slots > 0
                                            ? "green"
                                            : "red",
                                    fontWeight: "bold",
                                }}
                            >
                                {parking.available_slots}
                            </td>

                            <td>
                                {parking.available_slots > 0
                                    ? "🟢 Available"
                                    : "🔴 Full"}
                            </td>

                            <td>
                                {parking.available_slots > 0 ? (
                                    <button
                                        className="navigate-btn"
                                        onClick={() => handleNavigate(parking)}
                                    >
                                        🧭 Navigate
                                    </button>
                                ) : (
                                    <button
                                        className="full-btn"
                                        disabled
                                    >
                                        Full
                                    </button>
                                )}
                            </td>

                        </tr>
                    ))}
                </tbody>

            </table>

            {showDirections && selectedParking && (
                <div className="directions-popup">

                    <div className="popup-content">

                        <h2>📍 {selectedParking.zone_name}</h2>

                        <h3>Directions</h3>

                        <p style={{ whiteSpace: "pre-line",fontWeight: "bold" }}>
                            {selectedParking.directions}
                        </p>

                        <button
                            onClick={() => setShowDirections(false)}
                        >
                            ✓ Got it
                        </button>

                    </div>

                </div>
            )}

        </section>
    );
}

export default ParkingZones;