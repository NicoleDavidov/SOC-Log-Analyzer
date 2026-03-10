export async function fetchAlerts() {
  const res = await fetch("http://localhost:5000/alerts")
  return res.json()
}

export async function fetchRiskScores() {
  const res = await fetch("http://localhost:5000/risk-scores")
  return res.json()
}