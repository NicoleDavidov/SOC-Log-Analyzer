import AlertTable from "./components/AlertTable";
import RiskOverview from "./components/RiskOverview";
import AlertChart from "./components/AlertChart";

function App() {
  return (
    <div style={{
      minHeight: "100vh",
      backgroundColor: "#0f172a",
      padding: "20px",
      fontFamily: "Arial"
    }}>
      
      <h1 style={{color:"white", marginBottom:"20px"}}>
        SOC Monitoring Dashboard
      </h1>

      <RiskOverview />
      <AlertChart />
      <AlertTable />

    </div>
  );
}

export default App;