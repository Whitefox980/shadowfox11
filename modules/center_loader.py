import json

def load_center_data(path='db/center.json'):
    with open(path, 'r') as f:
        return json.load(f)

def get_headers(data, domain):
    return data["headers"] if data["targets"].get(domain, {}).get("custom_headers") else {}

def get_payloads(data, attack_type):
    return data["payloads"].get(attack_type, [])

def get_targets(data):
    return data["targets"]

def get_obfuscation_modes(data):
    return data["obfuscation_modes"]
