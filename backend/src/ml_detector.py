from sklearn.ensemble import IsolationForest
from collections import defaultdict
from datetime import datetime

def extract_features(logs):
    ip_stats = defaultdict(lambda: {
        "failed": 0,
        "success": 0,
        "users": set(),
        "night": 0
    })

    for log in logs:
        ip = log["ip"]
        user = log["user"]
        action = log["action"]

        ip_stats[ip]["users"].add(user)

        if action == "login_failed":
            ip_stats[ip]["failed"] += 1
        elif action == "login_success":
            ip_stats[ip]["success"] += 1

        time = datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S")
        if time.hour < 6 or time.hour > 22:
            ip_stats[ip]["night"] += 1

    features = []
    ips = []

    for ip, data in ip_stats.items():
        features.append([
            data["failed"],
            data["success"],
            len(data["users"]),
            data["night"]
        ])
        ips.append(ip)

    return features, ips


def detect_anomalies(logs):
    features, ips = extract_features(logs)

    if len(features) < 2:
        return []

    model = IsolationForest(contamination=0.3, random_state=42)
    model.fit(features)

    predictions = model.predict(features)
    scores = model.decision_function(features)

    alerts = []

    for i, pred in enumerate(predictions):
        if pred == -1:
            alerts.append({
                "type": "ANOMALY",
                "severity": "HIGH",
                "message": f"Unusual behavior detected from IP {ips[i]} (score={round(scores[i], 3)})"
            })

    return alerts