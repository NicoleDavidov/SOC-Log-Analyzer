import { useEffect, useState } from "react";
import { fetchAlerts } from "../services/api";

function AlertTable() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetchAlerts().then(setAlerts);
  }, []);

  return (
    <div>
      <h2>Detected Alerts</h2>
      <table border="1">
        <thead>
          <tr>
            <th>IP</th>
            <th>Type</th>
            <th>Severity</th>
          </tr>
        </thead>
        <tbody>
          {alerts.map((alert, index) => (
            <tr key={index}>
              <td>{alert.ip}</td>
              <td>{alert.type}</td>
              <td>{alert.severity}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AlertTable;