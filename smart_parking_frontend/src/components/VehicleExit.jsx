import { useState } from "react";

function VehicleExit() {

    const [vehicleId, setVehicleId] = useState("");
    const [message, setMessage] = useState("");

    async function handleSubmit(event) {
        event.preventDefault();

        const exitData = {
            vehicle_id: vehicleId
        };

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/parking/exit",
                {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(exitData)
                }
            );

            const result = await response.json();

            if (response.ok) {

                setMessage(result.message);
                setVehicleId("");

            } else {

                setMessage(result.detail);

            }

        } catch (error) {

            console.log("Error:", error);
            setMessage("Unable to connect to the server.");

        }
    }

    return (
        <section id="vehicle-exit" className="vehicle-exit">

            <h2>🚗 Vehicle Exit</h2>

            <form onSubmit={handleSubmit}>

                <label>Vehicle Number</label>

                <input
                    type="text"
                    placeholder="Enter Vehicle Number"
                    value={vehicleId}
                    onChange={(event) =>
                        setVehicleId(event.target.value)
                    }
                />

                <button type="submit">
                    Exit Vehicle
                </button>

            </form>

            {message && (
                <p className="success-message">
                    {message}
                </p>
            )}

        </section>
    );
}

export default VehicleExit;