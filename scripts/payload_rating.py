import os
import json
from collections import Counter

def rate_payloads(vector="xss"):
    log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs", "snapshots", "live_log.txt"))
    payloads = []

    with open(log_path, "r") as f:
        for line in f:
            if f"[SCORE" in line and f"?q=" in line and vector in line.lower():
                try:
                    payload = line.strip().split("?q=")[1]
                    payloads.append(payload)
                except:
                    continue

    top = Counter(payloads).most_common(10)
    print(f"\n[Top Payloads - {vector.upper()}]")
    for p, count in top:
        print(f"{count}x :: {p}")

if __name__ == "__main__":
    rate_payloads("xss")
