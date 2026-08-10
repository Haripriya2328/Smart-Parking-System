import './App.css'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import ParkingZones from "./components/ParkingZones";
import SearchBar from './components/SearchBar'
import Dashboard from "./components/Dashboard";
import VehicleEntry from "./components/VehicleEntry";
import VehicleExit from "./components/VehicleExit";

function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <ParkingZones />
      <SearchBar />
      <Dashboard />
      <VehicleEntry />
      <VehicleExit />
      
    </>
  )

}

export default App