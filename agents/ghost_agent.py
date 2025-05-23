import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core")))

import requests
from core_loader import get_targets_from_missions, get_attack_profile

def run_ghost_crawl():
    targets = get_targets_from_missions()
    profile = get_attack_profile("GhostCrawl")

    if profile is None:
        print("[GHOST] Nema definisan profil GhostCrawl!")
        return

    headers = profile.get("headers", {})

    for mission_id, url in targets:
        try:
            print(f"[GHOST] HEAD zahtev na {url}")
            r = requests.head(url, headers=headers, timeout=5)
            print(f"[{r.status_code}] {url}")
        except Exception as e:
            print(f"[!] Greška: {url} -> {e}")
