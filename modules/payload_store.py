from core_loader import connect_db
import datetime

def store_payload(payload, vector):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO payloads (code, vector, used, last_used) VALUES (?, ?, 0, ?)",
                (payload, vector, datetime.datetime.now()))
    conn.commit()
    conn.close()

def get_payloads_by_vector(vector):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, code FROM payloads WHERE vector = ?", (vector,))
    results = cur.fetchall()
    conn.close()
    return results
