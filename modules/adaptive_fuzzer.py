# modules/adaptive_fuzzer.py
import requests
from modules.mutation_engine import generate_payloads
from modules.confirmator import confirm_hit

TARGETS_FILE = "targets.txt"
LOG_FILE = "reports/raw_hits.log"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:124.0) Gecko/20100101 Firefox/124.0",
    "X-Forwarded-For": "127.0.0.1",
    "Referer": "https://google.com",
    "X-Custom-Stealth": "shadowfox"
}

def run_attack():
    with open(TARGETS_FILE, "r") as f:
        targets = [line.strip() for line in f if line.strip()]
    
    for target in targets:
        for payload_entry in generate_payloads():
            payload = payload_entry["payload"]
            ptype = payload_entry["type"]
            if "FUZZ" not in target:
                continue
            url = target.replace("FUZZ", requests.utils.quote(payload))
            try:
                r = requests.get(url, headers=HEADERS, timeout=6)
                with open(LOG_FILE, "a") as logf:
                    logf.write(f"[{r.status_code}] :: {url}\n")
                confirm_hit(url, payload, ptype, r.status_code)
            except Exception:
                continue

if __name__ == "__main__":
    run_attack()
