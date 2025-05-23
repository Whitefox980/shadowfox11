from core_loader import get_targets_from_missions, get_attack_profile

def assign_mission(profile_name="DefaultHuman"):
    targets = get_targets_from_missions()
    profile = get_attack_profile(profile_name)

    if not targets:
        print("[MISSION] Nema novih meta.")
        return

    for mission_id, url in targets:
        print(f"[MISSION] Izvršavam: {url} sa stilom: {profile_name}")
        print(f"[HEADERS] {profile['headers']}")
        print(f"[OBFUSCATION] {profile['obfuscation']}")
        # Ovde bi išao fuzz modul po izboru
