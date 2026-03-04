const BASE_URL = "http://localhost:5000";

export const fetchAlerts = async () => {
  const res = await fetch(`${BASE_URL}/alerts`);
  return res.json();
};

export const fetchRiskScores = async () => {
  const res = await fetch(`${BASE_URL}/risk-scores`);
  return res.json();
};