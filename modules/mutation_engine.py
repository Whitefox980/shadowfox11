import random

def generate_mutations(payload, count=3):
    mutations = [payload]
    for _ in range(count):
        variant = payload
        if "<" in variant:
            variant = variant.replace("<", random.choice(["<", "&#x3C;", "%3C"]))
        if ">" in variant:
            variant = variant.replace(">", random.choice([">", "&#x3E;", "%3E"]))
        if "(" in variant:
            variant = variant.replace("(", random.choice(["(", "%28"]))
        if ")" in variant:
            variant = variant.replace(")", random.choice([")", "%29"]))
        if "\"" in variant:
            variant = variant.replace("\"", random.choice(["%22", "&quot;", "\""]))
        mutations.append(variant)
    return list(set(mutations))
