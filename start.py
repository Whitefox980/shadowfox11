# start.py

import os
from modules.param_fuzzer import common_params as default_fuzz_params

base_urls = [
    "https://kayak.ai",
    "https://www.hotelscombined.com",
    "https://www.checkfelix.com/search"
]

def generate_targets_txt():
    with open("targets.txt", "w") as f:
        for url in base_urls:
            for param in default_fuzz_params:
                fuzz_url = f"{url}?{param}=FUZZ"
                f.write(f"{fuzz_url},xss,2\n")
    print("[✓] targets.txt generisan.")

def load_targets():
    print("[✓] Učitavam mete u queue...")
    os.system("python3 tools/load_targets.py")

def start_attack():
    print("[✓] Pokrećem AUTO MODE...")
    os.system("python3 main/auto_mode.py")

if __name__ == "__main__":
    generate_targets_txt()
    load_targets()
    start_attack()
