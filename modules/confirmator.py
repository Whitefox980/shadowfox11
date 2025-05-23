# modules/confirmator.py
import requests, json, os

CONFIRMED_FILE = "reports/confirmed_hits.json"

def confirm_hit(url, payload, ptype, status):
    try:
        r = requests.get(url, timeout=5)
        if payload[:8] in r.text or r.status_code == 200:
            hit = {
                "url": url,
                "payload": payload,
                "status": status,
                "type": ptype
            }
            os.makedirs("reports", exist_ok=True)
            with open(CONFIRMED_FILE, "a") as f:
                f.write(json.dumps(hit) + "\n")
    except:
        pass
