#Brute Force Detection
def detect_brute_force(logs, threshold=3):
    failed_attempts = {}

    for log in logs:
        if log["action"] == "login_failed":
            ip = log["ip"]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    alerts = []
    for ip, count in failed_attempts.items():
        if count >= threshold:
            alerts.append(f"Brute force suspected from IP {ip} ({count} failed attempts)")

    return alerts

#Detecting access during suspicious hours
from datetime import datetime

def detect_suspicious_hours(logs):
    alerts = []

    for log in logs:
        if log["action"] == "login_success":
            time = datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S")
            hour = time.hour

            if hour < 6 or hour > 22:
                alerts.append(f"Suspicious login time for user {log['user']} at {log['timestamp']}")

    return alerts
