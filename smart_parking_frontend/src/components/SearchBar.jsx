import { useState } from "react";

function SearchBar() {

    const [location, setLocation] = useState("");
    const [parkingData, setParkingData] = useState([]);

    async function handleSearch() {

        try {

            let url = "";

            if (location.trim() === "") {

                url = "http://127.0.0.1:8000/parking";

            } else {

                url = `http://127.0.0.1:8000/parking/search?name=${encodeURIComponent(location)}`;

            }

            const response = await fetch(url);

            if (!response.ok) {
                throw new Error("Parking zone not found");
            }

            const data = await response.json();

            if (Array.isArray(data)) {
                setParkingData(data);
            } else {
                setParkingData([data]);
            }

        } catch (error) {

            alert(error.message);
            setParkingData([]);

        }
    }

    return (
        <section id="search">

            <input
                type="text"
                placeholder="Enter parking location..."
                value={location}
                onChange={(event) =>
                    setLocation(event.target.value)
                }
            />

            <button onClick={handleSearch}>
                Search
            </button>

            <p>You typed: {location}</p>

            {parkingData.map((parking) => (

                <div
                    className="parking-card"
                    key={parking.zone_id}
                >

                    <h3>🚗 {parking.zone_name}</h3>

                    <p>
                        <strong>Capacity:</strong>{" "}
                        {parking.capacity}
                    </p>

                    <p>
                        <strong>Occupied:</strong>{" "}
                        {parking.occupied_slots}
                    </p>

                    <p>
                        <strong>Available:</strong>{" "}
                        {parking.available_slots}
                    </p>

                    {parking.available_slots > 0 ? (

                        <span className="status available">
                            🟢 Available
                        </span>

                    ) : (

                        <span className="status full">
                            🔴 Full
                        </span>

                    )}

                </div>

            ))}

        </section>
    );
}

export default SearchBar;