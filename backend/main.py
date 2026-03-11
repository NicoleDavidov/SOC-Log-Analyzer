import os
import json
from datetime import datetime

from src.log_generator import generate_logs
from src.analyzer import (
    analyze_logs,
    calculate_risk_scores,
    get_risk_level,
)
from src.parser import load_logs_from_json


# =========================
# Mode selection
# =========================
MODE = "generate"
# MODE = "load"


def main():
    # =========================
    # Base & Output directories
    # =========================
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOGS_DIR = os.path.join(BASE_DIR, "logs")
    OUTPUT_DIR = os.path.join(BASE_DIR, "output")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # =========================
    # Load logs (JSON or Generate)
    # =========================
    json_path = os.path.join(LOGS_DIR, "sample_logs.json")

    if MODE == "load" and os.path.exists(json_path):
        print("Loading logs from JSON file...\n")
        logs = load_logs_from_json(json_path)

    else:
        print("Generating simulated logs...\n")
        logs = generate_logs()

    # =========================
    # Analyze logs
    # =========================
    alerts = analyze_logs(logs)
    
    # Sort alerts by timestamp (newest first)
    alerts.sort(
        key=lambda x: datetime.strptime(x["timestamp"], "%Y-%m-%d %H:%M:%S"),
        reverse=True
    )

    # =========================
    # Print Alerts
    # =========================
    print("=== Security Alerts ===")
    for alert in alerts:
        print(f"{alert['timestamp']} - [{alert['severity']}] - {alert['type']} - {alert['message']}")

    # =========================
    # Risk Scores
    # =========================
    print("\n=== RISK SCORES ===")

    risk_scores = calculate_risk_scores(alerts)

    for ip, score in sorted(risk_scores.items(), key=lambda x: x[1], reverse=True):
        level = get_risk_level(score)
        print(f"{ip} -> Score: {score} ({level})")

    # =========================
    # Save results (INSIDE BACKEND/OUTPUT)
    # =========================
    alerts_path = os.path.join(OUTPUT_DIR, "alerts.json")
    risk_path = os.path.join(OUTPUT_DIR, "risk_scores.json")

    with open(alerts_path, "w") as f:
        json.dump(alerts, f, indent=4)

    with open(risk_path, "w") as f:
        json.dump(risk_scores, f, indent=4)

    # =========================
    # Summary
    # =========================
    print("\n=== SUMMARY ===")

    total = len(alerts)
    high = sum(1 for a in alerts if a['severity'] == 'HIGH')
    medium = sum(1 for a in alerts if a['severity'] == 'MEDIUM')
    low = sum(1 for a in alerts if a['severity'] == 'LOW')

    print(f"Total alerts: {total}")
    print(f"HIGH: {high} | MEDIUM: {medium} | LOW: {low}")

    print(f"\nResults saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()