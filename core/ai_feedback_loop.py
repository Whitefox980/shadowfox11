import os
import json
from random import choice

MIND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "shadow_mind.json"))

def suggest_payloads(vector="xss", count=3):
    with open(MIND_PATH, "r") as f:
        data = json.load(f)

    known = data.get(vector, [])
    if not known:
        return []

    return [choice(known) for _ in range(min(count, len(known)))]
