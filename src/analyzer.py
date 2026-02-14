from src.detector import detect_brute_force, detect_suspicious_hours

def analyze_logs(logs):
    alerts = []

    alerts.extend(detect_brute_force(logs))
    alerts.extend(detect_suspicious_hours(logs))

    return alerts
