# 🚗 Smart Parking System

## 📌 Project Overview

The **Smart Parking System** is a full-stack web application developed
to simplify parking zone management and help users find available
parking spaces.

The application provides a **React-based frontend**, a **FastAPI
backend**, and a **PostgreSQL database**. It supports parking zone
management, parking search, dashboard statistics, vehicle entry and
exit, and parking history.

The project demonstrates REST API development, CRUD operations,
PostgreSQL database integration, frontend-backend communication, form
validation, and dashboard-based data presentation.

------------------------------------------------------------------------

## ✨ Features

-   View all parking zones
-   Search parking zones by name
-   Find the nearest parking zone using latitude and longitude
-   View a parking zone by ID
-   Add new parking zones
-   Update parking zone information
-   Delete parking zones
-   Dashboard with parking statistics
-   Display total parking capacity
-   Display occupied and available slots
-   Vehicle entry management
-   Vehicle exit management
-   Parking history
-   Vehicle-specific parking history
-   Form validation
-   Responsive React user interface
-   REST API integration using FastAPI
-   PostgreSQL database integration

------------------------------------------------------------------------

## 🛠️ Technology Stack

### Frontend

-   React
-   Vite
-   JavaScript (ES6)
-   CSS
-   Fetch API

### Backend

-   Python
-   FastAPI
-   Uvicorn
-   Pydantic

### Database

-   PostgreSQL
-   psycopg2

### Development Tools

-   Visual Studio Code
-   Git
-   GitHub
-   Swagger / OpenAPI

------------------------------------------------------------------------

## 🏗️ Project Architecture

``` text
React Frontend
      │
      │ HTTP Requests / Fetch API
      ▼
FastAPI Backend
      │
      │ SQL Queries
      ▼
PostgreSQL Database
```

The React frontend communicates with the FastAPI backend through REST
APIs. The backend handles application logic and database operations
using PostgreSQL.

------------------------------------------------------------------------

## 📂 Project Structure

``` text
Smart-Parking-System/
│
├── backend/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── parking_routes.py
│   │   ├── vehicle_routes.py
│   │   ├── dashboard_routes.py
│   │   └── history_routes.py
│   │
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
│
├── smart_parking_frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   │   └── hero.png
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── ParkingZones.jsx
│   │   │   ├── SearchBar.jsx
│   │   │   ├── VehicleEntry.jsx
│   │   │   └── VehicleExit.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── eslint.config.js
│
├── screenshots/
├── .gitignore
├── LICENSE
└── README.md
```

> `node_modules`, Python cache files, and `.env` are excluded from
> version control using `.gitignore`.

------------------------------------------------------------------------

## 🗄️ Database

The application uses PostgreSQL to store parking information and related
application data.

### Parking Table

  Column              Description
  ------------------- ------------------------------------------
  `zone_id`           Unique parking zone ID
  `zone_name`         Parking zone name
  `capacity`          Total parking capacity
  `occupied_slots`    Number of occupied slots
  `available_slots`   Number of available slots
  `latitude`          Parking zone latitude
  `longitude`         Parking zone longitude
  `directions`        Directions for reaching the parking zone

------------------------------------------------------------------------

## 🌐 REST API Endpoints

### General

  Method   Endpoint   Description
  -------- ---------- -----------------
  GET      `/`        Welcome message

### Parking Management

  -----------------------------------------------------------------------------------------
  Method                  Endpoint                                  Description
  ----------------------- ----------------------------------------- -----------------------
  GET                     `/parking`                                Retrieve all parking
                                                                    zones

  GET                     `/parking/search?name=`                   Search parking zone by
                                                                    name

  GET                     `/parking/nearest?latitude=&longitude=`   Find nearest parking
                                                                    zone

  GET                     `/parking/id/{zone_id}`                   Retrieve parking zone
                                                                    by ID

  POST                    `/parking`                                Add a new parking zone

  PUT                     `/parking/update/{zone_id}`               Update an existing
                                                                    parking zone

  DELETE                  `/parking/{zone_id}`                      Delete a parking zone
  -----------------------------------------------------------------------------------------

### Vehicle Management

  Method   Endpoint           Description
  -------- ------------------ ----------------------
  POST     `/parking/entry`   Record vehicle entry
  PUT      `/parking/exit`    Record vehicle exit

### Dashboard

  Method   Endpoint       Description
  -------- -------------- ---------------------------------------
  GET      `/dashboard`   Retrieve parking dashboard statistics

### Parking History

  ---------------------------------------------------------------------------------
  Method                  Endpoint                          Description
  ----------------------- --------------------------------- -----------------------
  GET                     `/parking/history`                Retrieve parking
                                                            history

  GET                     `/parking/history/{vehicle_id}`   Retrieve history for a
                                                            specific vehicle
  ---------------------------------------------------------------------------------

------------------------------------------------------------------------

## 📊 Dashboard

The dashboard displays important parking statistics such as:

-   Total parking zones
-   Total parking capacity
-   Total occupied slots
-   Total available slots
-   Vehicles currently parked

This allows parking information to be viewed in a centralized dashboard.

------------------------------------------------------------------------

## 🚘 Vehicle Entry and Exit

The system supports vehicle entry and exit operations.

When a vehicle enters the parking system, the application records the
vehicle information and updates parking availability.

When a vehicle exits, the system updates the parking status and
maintains parking history.

------------------------------------------------------------------------

## 🔎 Parking Search

Users can search for a parking zone by name.

The application also supports finding the nearest parking zone using:

-   Latitude
-   Longitude

The backend calculates the distance between the provided location and
available parking zones.

------------------------------------------------------------------------

## ⚙️ Installation and Setup

### 1. Clone the repository

``` bash
git clone https://github.com/Haripriya2328/Smart-Parking-System.git
cd Smart-Parking-System
```

### 2. Backend setup

Create and activate a Python virtual environment if required:

``` bash
python -m venv venv
```

Windows:

``` bash
venv\Scripts\activate
```

Install backend dependencies:

``` bash
pip install -r backend/requirements.txt
```

### 3. Configure PostgreSQL

Create the PostgreSQL database:

``` text
smart_parking_db
```

Configure the database connection using environment variables in:

``` text
backend/.env
```

Example:

``` text
DB_HOST=localhost
DB_NAME=smart_parking_db
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
DB_PORT=5432
```

**Do not commit `.env` to GitHub.**

### 4. Start the FastAPI backend

``` bash
cd backend
uvicorn main:app --reload
```

The backend will normally be available at:

``` text
http://127.0.0.1:8000
```

FastAPI Swagger documentation is available at:

``` text
http://127.0.0.1:8000/docs
```

### 5. Start the React frontend

Open another terminal:

``` bash
cd smart_parking_frontend
npm install
npm run dev
```

Vite will display the local frontend URL in the terminal, normally:

``` text
http://localhost:5173
```

If that port is already in use, Vite may automatically select another
port.

------------------------------------------------------------------------

## 🔐 Environment Variables

Database credentials are stored locally in `.env`.

The `.env` file is excluded from Git using `.gitignore` to prevent
database credentials from being uploaded to GitHub.

------------------------------------------------------------------------

## 📸 Screenshots

The `screenshots/` folder contains screenshots demonstrating the
application and API functionality, including:

-   Dashboard overview
-   Parking table
-   Search functionality
-   Update parking
-   Delete confirmation
-   Validation
-   Swagger API documentation

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   Google Maps integration
-   Improved geolocation support
-   QR-code-based vehicle entry and exit
-   Parking slot reservation
-   Email notifications
-   Real-time parking availability updates
-   User authentication and role-based access
-   AI-based vehicle detection

------------------------------------------------------------------------

## 👩‍💻 Author

**Hari Priya Basam**

B.Tech Computer Science and Engineering\
Parul University

This project was developed as part of a full-stack development learning
journey using **React, FastAPI, PostgreSQL, and REST APIs**.
