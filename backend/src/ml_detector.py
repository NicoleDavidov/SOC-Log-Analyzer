from sklearn.ensemble import IsolationForest
from collections import defaultdict
from datetime import datetime


def extract_features(logs):

    ip_stats = defaultdict(lambda: {
        "failed": 0,
        "success": 0,
        "users": set(),
        "night": 0,
        "last_seen": None
    })

    for log in logs:

        ip = log["ip"]
        user = log["user"]
        action = log["action"]
        timestamp = log["timestamp"]

        ip_stats[ip]["users"].add(user)

        if action == "login_failed":
            ip_stats[ip]["failed"] += 1

        elif action == "login_success":
            ip_stats[ip]["success"] += 1

        time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

        if time.hour < 6 or time.hour > 22:
            ip_stats[ip]["night"] += 1

        # update last seen time
        if ip_stats[ip]["last_seen"] is None or timestamp > ip_stats[ip]["last_seen"]:
            ip_stats[ip]["last_seen"] = timestamp

    features = []
    ips = []
    timestamps = []

    for ip, data in ip_stats.items():

        features.append([
            data["failed"],
            data["success"],
            len(data["users"]),
            data["night"]
        ])

        ips.append(ip)
        timestamps.append(data["last_seen"])

    return features, ips, timestamps


def detect_anomalies(logs):

    features, ips, timestamps = extract_features(logs)

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
                "id": len(alerts) + 1,
                "timestamp": timestamps[i],
                "type": "ANOMALY",
                "severity": "HIGH",
                "score": round(scores[i], 3),
                "ip": ips[i],
                "message": f"Unusual behavior detected from IP {ips[i]} (score={round(scores[i],3)})"
            })

    return alerts