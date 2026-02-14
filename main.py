from src.parser import load_logs
from src.analyzer import analyze_logs

def main():
    logs = load_logs("logs/sample_logs.json")
    alerts = analyze_logs(logs)

    print("=== Security Alerts ===")
    for alert in alerts:
        print(alert)

if __name__ == "__main__":
    main()
