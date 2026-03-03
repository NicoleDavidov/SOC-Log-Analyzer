import os

from src.log_generator import generate_logs
from src.analyzer import (
    analyze_logs,
    calculate_risk_scores,
    get_risk_level,
    save_alerts_to_file,
    save_risk_scores
)
from src.parser import load_logs_from_json


def main():
    # =========================
    # Load logs (JSON or Generate)
    # =========================
    json_path = "logs/sample_logs.json"

    if os.path.exists(json_path):
        print("Loading logs from JSON file...\n")
        logs = load_logs_from_json(json_path)
    else:
        print("Generating simulated logs...\n")
        logs = generate_logs()

    # =========================
    # Analyze logs
    # =========================
    alerts = analyze_logs(logs)

    # =========================
    # Print Alerts
    # =========================
    print("=== Security Alerts ===")
    for alert in alerts:
        print(f"[{alert['severity']}] {alert['type']} - {alert['message']}")

    # =========================
    # Risk Scores
    # =========================
    print("\n=== RISK SCORES ===")

    risk_scores = calculate_risk_scores(alerts)

    for ip, score in sorted(risk_scores.items(), key=lambda x: x[1], reverse=True):
        level = get_risk_level(score)
        print(f"{ip} -> Score: {score} ({level})")

    # =========================
    # Save results
    # =========================
    save_alerts_to_file(alerts)
    save_risk_scores(risk_scores)

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


if __name__ == "__main__":
    main()