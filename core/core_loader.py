import json
import sqlite3

def load_shadowcore():
    with open("core/shadow_core.json", "r") as f:
        return json.load(f)

def get_attack_profile(name):
    data = load_shadowcore()
    for profile in data["attack_profiles"]:
        if profile["name"] == name:
            return profile
    return None

def connect_db():
    return sqlite3.connect("db/shadow_core.db")

def get_targets_from_missions(status="pending"):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, url FROM missions WHERE status=?", (status,))
    return cur.fetchall()
