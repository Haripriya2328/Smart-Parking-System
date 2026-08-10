import { useEffect, useState } from "react";

function Dashboard() {

    const [dashboard, setDashboard] = useState(null);

    useEffect(() => {
        fetchDashboard();
    }, []);

    async function fetchDashboard() {

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/dashboard"
            );

            if (!response.ok) {
                throw new Error("Failed to load dashboard");
            }

            const data = await response.json();

            setDashboard(data);

        } catch (error) {

            console.error(error);
            alert(error.message);

        }
    }

    if (!dashboard) {
        return <p>Loading Dashboard...</p>;
    }

    return (
        <section id="dashboard">

            <h2>📊 Parking Dashboard</h2>

            <div className="dashboard-container">

                <div className="dashboard-card">
                    <h3>🚗 Total Parking Zones</h3>
                    <p>{dashboard.total_parking_zones}</p>
                </div>

                <div className="dashboard-card">
                    <h3>🅿️ Total Capacity</h3>
                    <p>{dashboard.total_capacity}</p>
                </div>

                <div className="dashboard-card">
                    <h3>🚙 Occupied Slots</h3>
                    <p>{dashboard.total_occupied}</p>
                </div>

                <div className="dashboard-card">
                    <h3>✅ Available Slots</h3>
                    <p>{dashboard.total_available}</p>
                </div>

                <div className="dashboard-card">
                    <h3>🚘 Vehicles Parked</h3>
                    <p>{dashboard.vehicles_currently_parked}</p>
                </div>

            </div>

        </section>
    );
}

export default Dashboard;