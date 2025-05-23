# modules/config_loader.py
import json

def load_config(path="shadow_core.json"):
    with open(path, "r") as f:
        return json.load(f)
