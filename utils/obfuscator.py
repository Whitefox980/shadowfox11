def encode_payload(payload, method):
    if method == "charcode":
        return "".join(["&#" + str(ord(c)) + ";" for c in payload])
    elif method == "hex":
        return "".join(["\\x" + format(ord(c), "x") for c in payload])
    elif method == "unicode":
        return "".join(["\\u" + format(ord(c), "04x") for c in payload])
    else:
        return payload

def obfuscate_payload(payload, profile):
    encoded_versions = []
    for method in profile.get("obfuscation", {}).get("encoding", []):
        encoded = encode_payload(payload, method)
        encoded_versions.append(encoded)
    return encoded_versions if encoded_versions else [payload]
