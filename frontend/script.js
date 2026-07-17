// ========================================
// Get Buttons
// ========================================

// View Parking Button
const button = document.getElementById("loadBtn");

// Add Parking Button
const addButton = document.getElementById("addBtn");

// Search Button
const searchButton = document.getElementById("searchBtn");

// Stores the parking zone currently being edited
let editingZoneId=null;

// ========================================
// Button Events
// ========================================

// Load Parking Data
button.addEventListener("click", loadParking);

// Add Parking
addButton.addEventListener("click", addParking);

// Search Parking
searchButton.addEventListener("click", searchParking);

// ========================================
// Load Parking Data
// ========================================

function loadParking() {
    

    fetch("http://127.0.0.1:8000/parking")

    .then(response => response.json())

    .then(data => {
        let totalCapacity = 0;

        let occupied = 0;

        let available = 0;

        const table = document.getElementById("parkingTable");

        
        table.innerHTML = "";

        data.forEach(parking => {

            totalCapacity += parking.capacity;

            occupied += parking.occupied_slots;

            available += parking.available_slots;

            


            table.innerHTML += `
                <tr>
                    <td>${parking.zone_id}</td>
                    <td>${parking.zone_name}</td>
                    <td>${parking.capacity}</td>
                    <td>${parking.occupied_slots}</td>
                    <td>${parking.available_slots}</td>

                    <td>

                        <button 
                           class="editBtn"
                           onclick="editParking(${parking.zone_id})">

                           ✏ Edit
                        </button>

                        <button 
                            class="deleteBtn"
                            onclick="deleteParking(${parking.zone_id})">

                            🗑 Delete
                        </button>

                    </td>

                </tr>
            `;

        });

        document.getElementById("totalZones").textContent = data.length;

        document.getElementById("totalCapacity").textContent = totalCapacity;

        document.getElementById("occupiedSlots").textContent = occupied;

        document.getElementById("availableSlots").textContent = available;
        
        let percentage = 0;

        if (totalCapacity > 0) {

            percentage = (occupied / totalCapacity) * 100;

        }

        document.getElementById("occupancyPercentage").textContent =
            percentage.toFixed(2) + "%";

    })

    .catch(error => {

        console.log(error);

    });

}
// ========================================
// Add Parking / Update Parking
// ========================================

function addParking() {

    const zone_id = document.getElementById("zone_id").value;

    const zone_name = document.getElementById("zone_name").value;

    const capacity = document.getElementById("capacity").value;

    const occupied_slots = document.getElementById("occupied_slots").value;

    const available_slots = document.getElementById("available_slots").value;

     // ========================================
     // Validation
     // ========================================

    if (
        zone_id === "" ||
        zone_name.trim() === "" ||
        capacity === "" ||
        occupied_slots === "" ||
        available_slots === ""
    ) {

        alert("Please fill all the fields.");

      return;

    }
    if (Number(capacity)<=0){
        alert("Capacity must be greater than 0")
        return;
    }

    if (Number(occupied_slots)<0 || Number(available_slots)<0){
        alert("Occupied and Available slots cannot be negative.");
        return;
    }
    if (Number(occupied_slots)>Number(capacity)){
        alert("Occupied slots cannot be greater than capacity")
        return;
    }
    if(Number(available_slots)!==Number(capacity)-Number(occupied_slots)){
        alert("Available Slots must be equal to Capacity-Occupied_Slots");
        return;
    }

    const parking = {

        zone_id: Number(zone_id),

        zone_name: zone_name,

        capacity: Number(capacity),

        occupied_slots: Number(occupied_slots),

        available_slots: Number(available_slots)

    };

    // ========================================
    // Update Parking (PUT)
    // ========================================

    if (editingZoneId !== null) {

        fetch(`http://127.0.0.1:8000/parking/${editingZoneId}`, {

            method: "PUT",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(parking)

        })

        .then(response => response.json())

        .then(data => {

            alert(data.message);

            clearForm();

            editingZoneId = null;
           
            loadParking();

        })

        .catch(error => {

            console.log(error);

        });

        return;

    }

    // ========================================
    // Add Parking (POST)
    // ========================================

    fetch("http://127.0.0.1:8000/parking", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(parking)

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        clearForm();

        loadParking();

    })

    .catch(error => {

        console.log(error);

    });

}


// ========================================
// Delete Parking
// ========================================

function deleteParking(zone_id) {

    const confirmDelete = confirm("Are you sure you want to delete this parking zone?");

    if (!confirmDelete) {

        return;
    }

    fetch(`http://127.0.0.1:8000/parking/${zone_id}`, {

        method: "DELETE"

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        loadParking();

    })

    .catch(error => {

        console.log(error);

    });

}

// ========================================
// Edit Parking
// ========================================

function editParking(zone_id) {

    fetch(`http://127.0.0.1:8000/parking/${zone_id}`)

    .then(response => {

        return response.json();

    })

    .then(parking => {

        

        editingZoneId = zone_id;

        document.getElementById("zone_id").value = parking.zone_id;
        document.getElementById("zone_name").value = parking.zone_name;
        document.getElementById("capacity").value = parking.capacity;
        document.getElementById("occupied_slots").value = parking.occupied_slots;
        document.getElementById("available_slots").value = parking.available_slots;
        document.getElementById("modeText").textContent = "Mode: Update Parking";
        document.getElementById("addBtn").textContent = "Update Parking";
        
    })

    .catch(error => {

        console.log(error);
        alert("Unable to load parking details.")

    });

}

    
// ========================================
// Search Parking
// ========================================

function searchParking() {

    const name = document.getElementById("searchName").value;

    fetch(`http://127.0.0.1:8000/parking/search?name=${name}`)

    .then(response => response.json())

    .then(parking => {

        const table = document.getElementById("parkingTable");

        table.innerHTML = `
            <tr>

                <td>${parking.zone_id}</td>

                <td>${parking.zone_name}</td>

                <td>${parking.capacity}</td>

                <td>${parking.occupied_slots}</td>

                <td>${parking.available_slots}</td>

                <td>

                    <button class="editBtn" onclick="editParking(${parking.zone_id})">
                        ✏ Edit
                    </button>
                    <button class="deleteBtn" onclick="deleteParking(${parking.zone_id})">
                       🗑 Delete
                    </button>

                </td>

            </tr>
        `;

    })

    .catch(error => {

        console.log(error);

    });

}
// ========================================
// Clear Form
// ========================================

function clearForm(){

    document.getElementById("zone_id").value = "";

    document.getElementById("zone_name").value = "";

    document.getElementById("capacity").value = "";

    document.getElementById("occupied_slots").value = "";

    document.getElementById("available_slots").value = "";
    document.getElementById("modeText").textContent = "Mode: Add Parking";
    document.getElementById("addBtn").textContent = "Add Parking";

}