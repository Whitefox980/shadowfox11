import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "core")))

import time
import random

def simulate_user_behavior(profile):
    print("[OBSERVE] Simuliram ponašanje...")
    for _ in range(random.randint(2, 5)):
        delay = random.randint(*profile["behavior"]["click_delay_ms"])
        print(f"[*] Klik... čekam {delay}ms")
        time.sleep(delay / 1000)	
