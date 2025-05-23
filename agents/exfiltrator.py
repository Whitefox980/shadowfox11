import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "core")))
import sqlite3
import json
from core_loader import connect_db

def export_detections_to_json(file="reports/detections_export.json"):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM detections WHERE detected = 1")
    rows = cur.fetchall()
    keys = [description[0] for description in cur.description]
    results = [dict(zip(keys, row)) for row in rows]
    with open(file, "w") as f:
        json.dump(results, f, indent=4)
    print(f"[EXPORT] Sačuvano u: {file}")
