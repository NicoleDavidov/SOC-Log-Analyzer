import json
from collections import defaultdict
from datetime import datetime

BRUTE_FORCE_THRESHOLD = 5
MULTI_USER_THRESHOLD = 3

def load_logs():
    with open("logs.json", "r") as f:
        return json.load(f)

def analyze_logs(logs):
    alerts = []

    failed_attempts = defaultdict(int)
    success_after_fail = defaultdict(int)
    users_per_ip = defaultdict(set)

    for log in logs:
        ip = log["ip"]
        user = log["user"]
        action = log["action"]

        # Track users per IP
        users_per_ip[ip].add(user)

        if action == "login_fail":
            failed_attempts[ip] += 1

        elif action == "login_success":
            if failed_attempts[ip] > 0:
                alerts.append({
                    "type": "SUCCESS_AFTER_FAIL",
                    "severity": "HIGH",
                    "message": f"IP {ip} succeeded after {failed_attempts[ip]} failures"
                })
                failed_attempts[ip] = 0

    # Brute Force Detection
    for ip, count in failed_attempts.items():
        if count >= BRUTE_FORCE_THRESHOLD:
            alerts.append({
                "type": "BRUTE_FORCE",
                "severity": "HIGH",
                "message": f"{count} failed attempts from {ip}"
            })

    # Credential Stuffing
    for ip, users in users_per_ip.items():
        if len(users) >= MULTI_USER_THRESHOLD:
            alerts.append({
                "type": "CREDENTIAL_STUFFING",
                "severity": "MEDIUM",
                "message": f"{ip} tried {len(users)} different users"
            })

    # Suspicious login time
    for log in logs:
        hour = datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S").hour
        if log["action"] == "login_success" and (hour < 6 or hour > 23):
            alerts.append({
                "type": "SUSPICIOUS_TIME",
                "severity": "LOW",
                "message": f"{log['user']} logged in at {hour}:00 from {log['ip']}"
            })

    return alerts