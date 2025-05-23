import os
import json
from urllib.parse import urlparse

SIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "attack_signatures.json"))

def record_signature(url, payload, profile):
    host = urlparse(url).netloc
    sig = {
        "payload": payload,
        "profile": profile,
    }

    if not os.path.exists(SIG_PATH):
        with open(SIG_PATH, "w") as f:
            json.dump({}, f)

    with open(SIG_PATH, "r") as f:
        data = json.load(f)

    if host not in data:
        data[host] = []

    if sig not in data[host]:
        data[host].append(sig)

    with open(SIG_PATH, "w") as f:
        json.dump(data, f, indent=4)

def get_signatures_for_host(host):
    if not os.path.exists(SIG_PATH):
        return []
    with open(SIG_PATH, "r") as f:
        data = json.load(f)
    return data.get(host, [])
