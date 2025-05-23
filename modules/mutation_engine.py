import random

def evolve_payload(payload):
    mutations = [
        lambda p: p.replace("alert", "confirm"),
        lambda p: p.replace("<", "%3C"),
        lambda p: p.replace("1", "1337"),
        lambda p: p + "//",
        lambda p: p.upper()
    ]
    return random.choice(mutations)(payload)

def generate_mutations(base_payload, count=3):
    return [evolve_payload(base_payload) for _ in range(count)]
