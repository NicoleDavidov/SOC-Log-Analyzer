function AlertTable() {

  const alerts = [
    { id: 1, ip: "192.168.1.10", severity: "High", type: "Brute Force" },
    { id: 2, ip: "192.168.1.23", severity: "Medium", type: "Port Scan" },
    { id: 3, ip: "192.168.1.45", severity: "Low", type: "Login Attempt" },
  ];

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
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AlertTable;