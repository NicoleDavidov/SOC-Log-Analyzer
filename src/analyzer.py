import json
from collections import defaultdict
from datetime import datetime
from src.ml_detector import detect_anomalies

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