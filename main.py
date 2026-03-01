from src.log_generator import generate_logs
from src.analyzer import analyze_logs

def main():
    logs = generate_logs()
    alerts = analyze_logs(logs)

    print("=== Security Alerts ===")
    for alert in alerts:
        print(f"[{alert['severity']}] {alert['type']} - {alert['message']}")

if __name__ == "__main__":
    main()