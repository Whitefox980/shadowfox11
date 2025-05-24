import os
import json
from collections import Counter

MIND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "shadow_mind.json"))
SIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "attack_signatures.json"))

def suggest_profile_for_host(host):
    if not os.path.exists(SIG_PATH):
        return "DefaultHuman"

    with open(SIG_PATH, "r") as f:
        data = json.load(f)

    if host not in data:
        return "DefaultHuman"

    profiles = [e["profile"] for e in data[host]]
    counter = Counter(profiles)
    return counter.most_common(1)[0][0]

def top_payloads_for_vector(vector, limit=5):
    if not os.path.exists(MIND_PATH):
        return []

    with open(MIND_PATH, "r") as f:
        mind = json.load(f)

    if vector not in mind:
        return []

    counter = Counter(mind[vector])
    return [p for p, _ in counter.most_common(limit)]

def payloads_to_avoid(vector, min_threshold=2):
    if not os.path.exists(MIND_PATH):
        return []

    with open(MIND_PATH, "r") as f:
        mind = json.load(f)

    if vector not in mind:
        return []

    counter = Counter(mind[vector])
    return [p for p, c in counter.items() if c < min_threshold]
