import random

def evolve(payload):
    mutations = [
        lambda p: p.replace("<", "<<"),
        lambda p: p.replace(">", ">>"),
        lambda p: p.replace("script", "scr<script>ipt"),
        lambda p: p.upper(),
        lambda p: p + "//",
        lambda p: f'"{p}"',
        lambda p: p.replace("'", '"'),
        lambda p: p[::-1],  # reverse
    ]
    return random.choice(mutations)(payload)

def evolve_batch(payload, count=3):
    return [evolve(payload) for _ in range(count)]
