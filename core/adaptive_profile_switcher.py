import os
import json
from urllib.parse import urlparse

SWITCH_LOG = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "switch_log.json"))
THRESHOLD = 3  # koliko puta mora da padne da bi se promenio profil

def log_failure(url):
    host = urlparse(url).netloc
    if not os.path.exists(SWITCH_LOG):
        with open(SWITCH_LOG, "w") as f:
            json.dump({}, f)

    with open(SWITCH_LOG, "r") as f:
        data = json.load(f)

    data[host] = data.get(host, 0) + 1

    with open(SWITCH_LOG, "w") as f:
        json.dump(data, f, indent=4)

def should_switch(url):
    host = urlparse(url).netloc
    if not os.path.exists(SWITCH_LOG):
        return False
    with open(SWITCH_LOG, "r") as f:
        data = json.load(f)
    return data.get(host, 0) >= THRESHOLD

def reset_failure(url):
    host = urlparse(url).netloc
    if not os.path.exists(SWITCH_LOG):
        return
    with open(SWITCH_LOG, "r") as f:
        data = json.load(f)
    if host in data:
        del data[host]
    with open(SWITCH_LOG, "w") as f:
        json.dump(data, f, indent=4)
