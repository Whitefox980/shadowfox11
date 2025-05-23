import os

def run_all():
    print("\n[+] Pokrećem TARGET LOADER...")
    os.system("python3 tools/load_targets.py")

    print("\n[+] Pokrećem AUTO MODE NAPAD...")
    os.system("python3 main/auto_mode.py")

    print("\n[+] Pokrećem AI REPLAY (shadowbrain)...")
    os.system("python3 tools/shadowbrain_replay.py")

    print("\n[✓] Misija završena.")

if __name__ == "__main__":
    run_all()
