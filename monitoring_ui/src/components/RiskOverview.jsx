import { useEffect, useState } from "react";
import { fetchRiskScores } from "../services/api";

function RiskOverview() {
  const [riskScores, setRiskScores] = useState([]);

  useEffect(() => {
    fetchRiskScores().then(setRiskScores);
  }, []);

  return (
    <div>
      <h2>Risk Summary</h2>
      <p>Total Entities Monitored: {riskScores.length}</p>
    </div>
  );
}

export default RiskOverview;