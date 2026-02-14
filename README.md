# SOC Log Analyzer

A basic Security Operations Center (SOC) log analyzer written in Python. This project parses log files, detects potential security threats, and generates alerts.

## Features (current version)

- **Brute Force Detection:** Identifies IP addresses with multiple failed login attempts.  
- **Suspicious Login Time Detection:** Alerts on logins during unusual hours (e.g., late night).

## How to Run

Make sure you have Python 3 installed. Navigate to the project root folder in your terminal. (Optional) Install dependencies if listed in `requirements.txt` using `pip install -r requirements.txt`. Run the main script with `python main.py`. The program will display security alerts based on the sample logs in `logs/sample_logs.json`.

## Project Structure

SOC-LOG-ANALYZER/
│
├── logs/                  # Sample log files
│   └── sample_logs.json
├── src/
│   ├── __pycache__/       # Python cache (ignored by git)
│   ├── __init__.py        # Makes src a package
│   ├── analyzer.py        # Combines detectors and returns alerts
│   ├── detector.py        # Contains detection logic for alerts
│   └── parser.py          # Loads and parses log files
├── main.py                # Entry point for running the project
├── .gitignore             # Files/folders ignored by Git
├── requirements.txt       # Optional dependencies
└── README.md              # Project description



## Notes

This is the initial version of the SOC Log Analyzer. Future improvements can include additional detection rules and AI/ML-based anomaly detection.
