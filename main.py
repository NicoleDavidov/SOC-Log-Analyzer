from src.log_generator import generate_logs
from src.analyzer import analyze_logs

def main():
    logs = generate_logs()

    alerts = analyze_logs(logs)

    print("=== Security Alerts ===")
    for alert in alerts:
        print(f"[{alert['severity']}] {alert['type']} - {alert['message']}")

    print("\n=== SUMMARY ===")

    total = len(alerts)
    high = sum(1 for a in alerts if a['severity'] == 'HIGH')
    medium = sum(1 for a in alerts if a['severity'] == 'MEDIUM')
    low = sum(1 for a in alerts if a['severity'] == 'LOW')

    print(f"Total alerts: {total}")
    print(f"HIGH: {high} | MEDIUM: {medium} | LOW: {low}")

if __name__ == "__main__":
    main()