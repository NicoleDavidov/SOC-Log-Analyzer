import AlertTable from "./components/AlertTable";
import RiskOverview from "./components/RiskOverview";

function App() {
  return (
    <div style={{ backgroundColor: "#111", color: "#0f0", minHeight: "100vh", padding: "20px" }}>
      <h1>SOC Monitoring Console</h1>
      <RiskOverview />
      <AlertTable />
    </div>
  );
}

export default App;