import random

def encode_charcode(payload):
    return "".join([f"&#{ord(c)};" for c in payload])

def encode_unicode(payload):
    return "".join([f"\\u{ord(c):04x}" for c in payload])

def reverse_payload(payload):
    return payload[::-1]

def inject_noise(payload):
    return payload.replace("alert", "al<!--xx-->ert").replace("script", "scr<!--oo-->ipt")

def hex_wrap(payload):
    return "".join(["\\x" + format(ord(c), "x") for c in payload])

def bypass_variants(payload):
    variants = [
        payload,
        encode_charcode(payload),
        encode_unicode(payload),
        inject_noise(payload),
        reverse_payload(payload),
        hex_wrap(payload),
        f"`{payload}`",
        f"${{{payload}}}",
    ]
    return list(set(variants))  # ukloni duplikate
