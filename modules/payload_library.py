import os
import json

PAYLOAD_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "payloads.json"))

def load_payloads(vector):
    if not os.path.exists(PAYLOAD_PATH):
        return []
    with open(PAYLOAD_PATH, "r") as f:
        data = json.load(f)
    return data.get(vector, [])
