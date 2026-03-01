import random
from datetime import datetime, timedelta


# Basic data
IPS = ["192.168.1.10", "192.168.1.20", "10.0.0.5", "172.16.0.3"]
USERS = ["admin", "user1", "guest", "test"]


def random_timestamp():
    base_time = datetime.now()
    random_minutes = random.randint(0, 1440)
    time = base_time - timedelta(minutes=random_minutes)
    return time.strftime("%Y-%m-%d %H:%M:%S")


# Regular log
def generate_normal_log():
    return {
        "timestamp": random_timestamp(),
        "ip": random.choice(IPS),
        "user": random.choice(USERS),
        "action": random.choice(["login_success", "login_failed"])
    }


# Brute Force attack
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


# Success after Brute Force
def generate_success_after_bruteforce(ip):
    logs = generate_brute_force(ip)

    logs.append({
        "timestamp": random_timestamp(),
        "ip": ip,
        "user": "admin",
        "action": "login_success"
    })

    return logs


# Credential Stuffing
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


# Suspicious hours
def generate_suspicious_hour_log():
    time = datetime.now().replace(hour=random.choice([1, 2, 3]), minute=0, second=0)

    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "ip": random.choice(IPS),
        "user": "admin",
        "action": "login_success"
    }


# Main function
def generate_logs(num_logs=50):
    logs = []

    for _ in range(num_logs):
        logs.append(generate_normal_log())

    # Add attacks
    logs.extend(generate_brute_force("192.168.1.100"))
    logs.extend(generate_success_after_bruteforce("192.168.1.200"))
    logs.extend(generate_credential_stuffing("192.168.1.300"))

    for _ in range(3):
        logs.append(generate_suspicious_hour_log())

    return logs