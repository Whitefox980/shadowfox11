import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "modules")))

from shadow_task_queue import add_task
from param_fuzzer import find_fuzzable_param

FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "targets.txt"))

def load_targets():
    if not os.path.exists(FILE_PATH):
        print("[!] targets.txt ne postoji.")
        return

    with open(FILE_PATH, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                print(f"[X] Pogrešan format: {line}")
                continue
            url, vector, prio = parts
            try:
                prio = int(prio.strip())
                fuzzable = find_fuzzable_param(url.strip())
                if not fuzzable:
                    print(f"[X] Nema fuzz parametara za {url}")
                    continue
                for param in fuzzable:
                    fuzz_url = f"{url.strip()}?{param}=FUZZ"
                    add_task(fuzz_url, prio, vector.strip())
                    print(f"[+] Dodata meta: {fuzz_url} ({vector.strip()}, prio {prio})")
            except Exception as e:
                print(f"[X] Greška: {e}")

if __name__ == "__main__":
    load_targets()
