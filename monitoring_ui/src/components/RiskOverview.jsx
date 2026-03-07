function RiskOverview() {

  const box = {
    background:"#1e293b",
    padding:"20px",
    borderRadius:"10px",
    width:"200px",
    color:"white"
  }

  return (
    <div style={{
      display:"flex",
      gap:"20px"
    }}>

      <div style={box}>
        <h3>Total Alerts</h3>
        <h1>27</h1>
      </div>

      <div style={box}>
        <h3>High Risk</h3>
        <h1 style={{color:"#ef4444"}}>5</h1>
      </div>

      <div style={box}>
        <h3>Medium Risk</h3>
        <h1 style={{color:"#f59e0b"}}>12</h1>
      </div>

      <div style={box}>
        <h3>Low Risk</h3>
        <h1 style={{color:"#10b981"}}>10</h1>
      </div>

    </div>
  );
}

export default RiskOverview;