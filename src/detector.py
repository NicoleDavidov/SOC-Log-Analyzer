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

# Success after few failures
def detect_success_after_failures(logs, threshold=3):
    failed_attempts = {}
    alerts = []

    for log in logs:
        ip = log["ip"]
        action = log["action"]

        # failure
        if action == "login_failed":
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

        # Success
        elif action == "login_success":
            if failed_attempts.get(ip, 0) >= threshold:
                alerts.append(
                    f"Possible brute force success from IP {ip} "
                    f"after {failed_attempts[ip]} failed attempts"
                )
            # Reset after success
            failed_attempts[ip] = 0

    return alerts


#Credential Stuffing (multiple users from same IP)
def detect_multiple_users_from_same_ip(logs, threshold=3):
    ip_users = {}
    alerts = []

    for log in logs:
        ip = log["ip"]
        user = log["user"]

        # IP don't exist
        if ip not in ip_users:
            ip_users[ip] = set()  # set to keep unique users

        ip_users[ip].add(user)

    # test
    for ip, users in ip_users.items():
        if len(users) >= threshold:
            alerts.append(
                f"Suspicious activity: IP {ip} tried {len(users)} different users"
            )

    return alerts


