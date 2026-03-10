import { useEffect, useState } from "react";
import { fetchAlerts } from "../services/api";

function AlertTable() {

  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    async function loadAlerts() {
      const data = await fetchAlerts();
      setAlerts(data);
    }

    loadAlerts();
  }, []);

  const getSeverityColor = (severity) => {
    if (severity === "High") return "#ef4444";
    if (severity === "Medium") return "#f59e0b";
    return "#10b981";
  };

  return (
    <div
      style={{
        background: "#1e293b",
        padding: "20px",
        borderRadius: "10px",
        marginTop: "20px",
      }}
    >
      <h2 style={{ color: "white", marginBottom: "15px" }}>
        Recent Alerts
      </h2>

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          color: "white",
        }}
      >
        <thead>
          <tr style={{ textAlign: "left", borderBottom: "1px solid #334155" }}>
            <th style={{ padding: "10px" }}>ID</th>
            <th style={{ padding: "10px" }}>IP</th>
            <th style={{ padding: "10px" }}>Severity</th>
            <th style={{ padding: "10px" }}>Type</th>
            <th style={{ padding: "10px" }}>Message</th>
          </tr>
        </thead>

        <tbody>
          {alerts.map((alert) => (
            <tr
              key={alert.id}
              style={{
                borderBottom: "1px solid #334155",
              }}
            >
              <td style={{ padding: "10px" }}>{alert.id}</td>

              <td style={{ padding: "10px" }}>{alert.ip}</td>

              <td
                style={{
                  padding: "10px",
                  color: getSeverityColor(alert.severity),
                  fontWeight: "bold",
                }}
              >
                {alert.severity}
              </td>

              <td style={{ padding: "10px" }}>{alert.type}</td>

              <td style={{ padding: "10px" }}>{alert.message}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AlertTable;