import random
from datetime import datetime, timedelta


# Realistic internal network IPs
IPS = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30",
    "192.168.1.40",
    "192.168.1.50",
    "10.0.0.5",
    "10.0.0.15",
    "10.0.0.25",
    "172.16.0.3",
    "172.16.0.8"
]

USERS = ["admin", "user1", "user2", "guest", "test"]


# Generate realistic timestamp within last 24 hours
def random_timestamp():
    base_time = datetime.now()
    random_minutes = random.randint(0, 1440)
    time = base_time - timedelta(minutes=random_minutes)
    return time.strftime("%Y-%m-%d %H:%M:%S")


# --------------------
# Normal user activity
# --------------------
def generate_normal_log():
    return {
        "timestamp": random_timestamp(),
        "ip": random.choice(IPS),
        "user": random.choice(USERS),
        "action": random.choice(["login_success", "login_failed"])
    }


# --------------------
# Brute Force attack
# --------------------
def generate_brute_force(ip):
    logs = []
    user = random.choice(USERS)

    for _ in range(5):
        logs.append({
            "timestamp": random_timestamp(),
            "ip": ip,
            "user": user,
            "action": "login_failed"
        })

    return logs


# --------------------
# Success after brute force
# --------------------
def generate_success_after_bruteforce(ip):
    logs = generate_brute_force(ip)

    logs.append({
        "timestamp": random_timestamp(),
        "ip": ip,
        "user": "admin",
        "action": "login_success"
    })

    return logs


# --------------------
# Credential Stuffing
# --------------------
def generate_credential_stuffing(ip):
    logs = []

    for user in USERS:
        logs.append({
            "timestamp": random_timestamp(),
            "ip": ip,
            "user": user,
            "action": "login_failed"
        })

    return logs


# --------------------
# Suspicious login hour
# --------------------
def generate_suspicious_hour_log():
    time = datetime.now().replace(
        hour=random.choice([1, 2, 3]),
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )

    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "ip": random.choice(IPS),
        "user": "admin",
        "action": "login_success"
    }


# --------------------
# Main log generator
# --------------------
def generate_logs(num_logs=50):

    logs = []

    # Normal activity
    for _ in range(num_logs):
        logs.append(generate_normal_log())

    # Attacks with random IPs
    attack_ip1 = random.choice(IPS)
    attack_ip2 = random.choice(IPS)
    attack_ip3 = random.choice(IPS)

    logs.extend(generate_brute_force(attack_ip1))
    logs.extend(generate_success_after_bruteforce(attack_ip2))
    logs.extend(generate_credential_stuffing(attack_ip3))

    # Suspicious logins
    for _ in range(3):
        logs.append(generate_suspicious_hour_log())

    # Add unique ID to each log
    for i, log in enumerate(logs):
        log["id"] = i + 1

    return logs