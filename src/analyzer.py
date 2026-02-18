from src.detector import (
    detect_brute_force,
    detect_suspicious_hours,
    detect_success_after_failures,
    detect_multiple_users_from_same_ip
)

def analyze_logs(logs):
    alerts = []

    # Brute Force
    alerts.extend(detect_brute_force(logs))

    # Suspicious Hours
    alerts.extend(detect_suspicious_hours(logs))

    # Success after failures
    alerts.extend(detect_success_after_failures(logs))

    # Credential Stuffing (multiple users from same IP)
    alerts.extend(detect_multiple_users_from_same_ip(logs))

    return alerts

