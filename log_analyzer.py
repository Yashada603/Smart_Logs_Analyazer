import re
from collections import defaultdict

LOG_FILE = "sample_logs.txt"

failed_attempts = defaultdict(int)

failed_pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

def analyze_logs():
    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                match = failed_pattern.search(line)
                if match:
                    ip = match.group(1)
                    failed_attempts[ip] += 1

    except FileNotFoundError:
        print("Log file not found!")
        return

def detect_suspicious():
    print("\n=== Suspicious Activity Report ===\n")
    for ip, count in failed_attempts.items():
        if count >= 3:
            print(f"[ALERT] Possible brute-force attack from IP: {ip} (Attempts: {count})")
        else:
            print(f"[INFO] IP: {ip} (Attempts: {count})")

def main():
    analyze_logs()
    detect_suspicious()

if __name__ == "__main__":
    main()