import json
import os

def extract_hits(folder):
    results = []
    for fname in os.listdir(folder):
        if fname.endswith(".json"):
            with open(os.path.join(folder, fname)) as f:
                data = json.load(f)
                for entry in data:
                    if entry.get("status") == 200:
                        results.append((entry["url"], entry["payload"]))
    with open("reports/confirmed_hits_summary.txt", "w") as f:
        for url, payload in results:
            f.write(f"[OK]  {url} → {payload}\n")
    print(f"[✓] Završeno. Pronađeno {len(results)} potvrđenih hitova.")

extract_hits("reports")
