import json
from collections import defaultdict
from datetime import datetime
from src.ml_detector import detect_anomalies
import re

# =========================
# Configuration
# =========================
BRUTE_FORCE_THRESHOLD = 5
MULTI_USER_THRESHOLD = 3


# =========================
# Load logs (optional)
# =========================
def load_logs(file_path="logs.json"):
    with open(file_path, "r") as f:
        return json.load(f)


# =========================
# Main Analysis Function
# =========================
def analyze_logs(logs):
    alerts = []

    failed_attempts = defaultdict(int)
    users_per_ip = defaultdict(set)

    # =========================
    # First pass - collect data
    # =========================
    for log in logs:
        ip = log.get("ip")
        user = log.get("user")
        action = log.get("action")

        # Track how many users per IP
        users_per_ip[ip].add(user)

        if action == "login_fail":
            failed_attempts[ip] += 1

        elif action == "login_success":
            # Success after fails (Brute force success)
            if failed_attempts[ip] > 0:
                alerts.append({
                    "type": "SUCCESS_AFTER_FAIL",
                    "severity": "HIGH",
                    "message": f"IP {ip} succeeded after {failed_attempts[ip]} failures"
                })
                # Reset counter after success
                failed_attempts[ip] = 0

    # =========================
    # Brute Force Detection
    # =========================
    for ip, count in failed_attempts.items():
        if count >= BRUTE_FORCE_THRESHOLD:
            alerts.append({
                "type": "BRUTE_FORCE",
                "severity": "HIGH",
                "message": f"{count} failed attempts from {ip}"
            })

    # =========================
    # Credential Stuffing Detection
    # =========================
    for ip, users in users_per_ip.items():
        if len(users) >= MULTI_USER_THRESHOLD:
            alerts.append({
                "type": "CREDENTIAL_STUFFING",
                "severity": "MEDIUM",
                "message": f"{ip} tried {len(users)} different users"
            })

    # =========================
    # Suspicious Login Time
    # =========================
    for log in logs:
        try:
            timestamp = log.get("timestamp")
            hour = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").hour

            if log.get("action") == "login_success" and (hour < 6 or hour > 23):
                alerts.append({
                    "type": "SUSPICIOUS_TIME",
                    "severity": "LOW",
                    "message": f"{log.get('user')} logged in at {hour}:00 from {log.get('ip')}"
                })
        except Exception:
            # skip invalid timestamps
            continue

    # =========================
    # AI / ML Anomaly Detection
    # =========================
    try:
        anomalies = detect_anomalies(logs)
        alerts.extend(anomalies)
    except Exception as e:
        print("AI detection failed:", e)

    return alerts



# Risk Score
def calculate_risk_scores(alerts):
    risk_scores = defaultdict(int)

    for alert in alerts:
        ip = extract_ip(alert["message"])

        if not ip:
            continue

        if alert["severity"] == "HIGH":
            risk_scores[ip] += 10
        elif alert["severity"] == "MEDIUM":
            risk_scores[ip] += 5
        elif alert["severity"] == "LOW":
            risk_scores[ip] += 2

    return risk_scores

# Function that extracts IP from text
def extract_ip(message):
    match = re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", message)
    return match.group(0) if match else None

def get_risk_level(score):
    if score >= 30:
        return "CRITICAL"
    elif score >= 15:
        return "HIGH"
    elif score >= 5:
        return "MEDIUM"
    else:
        return "LOW"
    
# Save to file function
def save_alerts_to_file(alerts, filename="alerts.json"):
    import json

    with open(filename, "w") as f:
        json.dump(alerts, f, indent=4)

# Maintaining Risk Scores as well
def save_risk_scores(risk_scores, filename="risk_scores.json"):
    import json

    data = []

    for ip, score in risk_scores.items():
        data.append({
            "ip": ip,
            "score": score,
            "level": get_risk_level(score)
        })

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)