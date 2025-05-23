import json
import os

MIND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "shadow_mind.json"))

def record_hit(vector, payload):
    with open(MIND_PATH, "r") as f:
        data = json.load(f)

    if vector not in data:
        data[vector] = []

    if payload not in data[vector]:
        data[vector].append(payload)

    with open(MIND_PATH, "w") as f:
        json.dump(data, f, indent=4)

def get_brain_payloads(vector):
    with open(MIND_PATH, "r") as f:
        data = json.load(f)
    return data.get(vector, [])
