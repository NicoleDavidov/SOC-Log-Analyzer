from sklearn.ensemble import IsolationForest
import numpy as np


class AIAnalyzer:
    def __init__(self):
        # model for anomaly detection
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.trained = False

    def extract_features(self, logs):
        """
        Convert logs into numeric features per IP
        """
        ip_data = {}

        for log in logs:
            ip = log["ip"]
            status = log["status"]
            action = log["action"]

            if ip not in ip_data:
                ip_data[ip] = {
                    "fail": 0,
                    "success": 0,
                    "login": 0
                }

            if status == "FAIL":
                ip_data[ip]["fail"] += 1
            else:
                ip_data[ip]["success"] += 1

            if action == "LOGIN":
                ip_data[ip]["login"] += 1

        # convert to matrix
        features = []
        ips = []

        for ip, data in ip_data.items():
            features.append([
                data["fail"],
                data["success"],
                data["login"]
            ])
            ips.append(ip)

        return np.array(features), ips

    def train(self, logs):
        X, _ = self.extract_features(logs)
        if len(X) > 0:
            self.model.fit(X)
            self.trained = True

    def detect_anomalies(self, logs):
        """
        Returns suspicious IPs based on anomaly detection
        """
        if not self.trained:
            self.train(logs)

        X, ips = self.extract_features(logs)

        if len(X) == 0:
            return []

        scores = self.model.decision_function(X)
        predictions = self.model.predict(X)

        anomalies = []

        for i in range(len(ips)):
            if predictions[i] == -1:
                anomalies.append({
                    "ip": ips[i],
                    "score": scores[i]
                })

        return anomalies