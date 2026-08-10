import { useState } from "react";

function VehicleEntry() {

    const [parkingId, setParkingId] = useState("");
    const [vehicleId, setVehicleId] = useState("");
    const [entryTime, setEntryTime] = useState("");
    const [message, setMessage] = useState("");

    async function handleSubmit(event) {

        event.preventDefault();

        const vehicleData = {
            parking_id: Number(parkingId),
            vehicle_id: vehicleId,
            entry_time: entryTime,
            exit_time: null,
            status: "Parked",
        };

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/parking/entry",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(vehicleData),
                }
            );

            const result = await response.json();

            if (response.ok) {

                setMessage(result.message);

                setParkingId("");
                setVehicleId("");
                setEntryTime("");

            } else {

                setMessage(result.detail);

            }

        } catch (error) {

            console.log("Error:", error);

            setMessage("Unable to connect to the server.");

        }
    }

    return (
        <section id="vehicle-entry" className="vehicle-entry">

            <h2>🚗 Vehicle Entry</h2>

            <form
                onSubmit={handleSubmit}
                className="vehicle-entry-form"
            >

                <div className="form-group">

                    <label>Parking Zone ID</label>

                    <input
                        type="number"
                        placeholder="Enter Parking Zone ID"
                        value={parkingId}
                        onChange={(event) =>
                            setParkingId(event.target.value)
                        }
                    />

                </div>

                <div className="form-group">

                    <label>Vehicle Number</label>

                    <input
                        type="text"
                        placeholder="Enter Vehicle Number"
                        value={vehicleId}
                        onChange={(event) =>
                            setVehicleId(event.target.value)
                        }
                    />

                </div>

                <div className="form-group">

                    <label>Entry Time</label>

                    <input
                        type="datetime-local"
                        value={entryTime}
                        onChange={(event) =>
                            setEntryTime(event.target.value)
                        }
                    />

                </div>

                <button type="submit">
                    Enter Vehicle
                </button>

                {message && (
                    <p className="message">
                        {message}
                    </p>
                )}

            </form>

        </section>
    );
}

export default VehicleEntry;