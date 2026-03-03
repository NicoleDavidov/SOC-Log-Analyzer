# SOC Log Analyzer – Backend

A Python-based Security Operations Center (SOC) log analysis engine.  
This backend parses authentication logs, detects suspicious activity patterns, assigns risk scores, and generates structured alerts for a monitoring dashboard.

---

## Features 

### 🔍 Detection Engine
- **Credential Stuffing Detection**  
  Detects multiple failed login attempts from the same IP across different usernames.

- **Success-After-Failure Detection**  
  Identifies cases where multiple failed login attempts are followed by a successful login.

- **Brute Force Detection**  
  Flags repeated failed login attempts from the same IP address.

### ⚠ Risk Scoring System
Each alert is assigned a calculated risk score based on:
- Number of failed attempts
- Login success after failures
- Pattern severity

Risk scores are stored in: `risk_scores.json`

### 📁 Structured Output
The analyzer generates:

- `alerts.json` – Detected security alerts  
- `risk_scores.json` – Calculated risk levels  
- `logs.json` – Parsed log data  

These outputs are designed to be consumed by a frontend dashboard.

---

## 🏗 Architecture

```
backend/
│
├── logs/ 
│   ├── sample_logs.json        # Log file (input data)
├── src/
│   ├── ai_modul.py             # 
│   ├── analyzer.py             # detection modules
│   ├── log_generator.py 
│   ├── ml_detector.py          # 
│   ├── parser.py               # Log parsing logic
│
├── main.py                     # Entry point
├── requirements.txt
└── README.md
```

---

## ▶ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the analyzer
```bash
python main.py
```

The program will:
- Parse log files
- Apply detection rules
- Generate alerts
- Calculate risk scores
- Output structured JSON files

---

### 🛠 Technologies
- Python 3
- JSON-based log processing
- Modular detection architecture
- Risk scoring engine

---

### 🎯 Project Purpose

This backend simulates a real SOC monitoring engine and is designed to integrate with a React-based dashboard for visualization and incident monitoring.

It demonstrates:
- Log parsing
- Security pattern detection
- Risk assessment logic
- Clean modular backend structure

---

### 🔮 Future Improvements
- Real-time log streaming
- Machine learning anomaly detection
- Database integration (PostgreSQL / MongoDB)
- REST API integration with Flask
- Docker deployment