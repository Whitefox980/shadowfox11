import time
import random

def pre_attack_probe(session, url, headers):
    test_payload = "shadow_probe"
    probe_url = url.replace("FUZZ", test_payload)
    try:
        start = time.time()
        r = session.get(probe_url, headers=headers, timeout=5)
        duration = time.time() - start
        if "access denied" in r.text.lower() or r.status_code in [403, 406]:
            return False, duration
        if duration > 3:
            return False, duration  # WAF delay
        return True, duration
    except:
        return False, 0
