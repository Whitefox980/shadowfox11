import os
import json
from collections import Counter
from urllib.parse import urlparse
from rich.table import Table
from rich.console import Console

MIND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "shadow_mind.json"))
SIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "attack_signatures.json"))

console = Console()

def analyze_shadowbrain():
    if not os.path.exists(MIND_PATH):
        console.print("[!] Nema shadow_mind.json fajla.", style="red")
        return

    with open(MIND_PATH, "r") as f:
        mind = json.load(f)

    top_payloads = Counter()
    for vector, payloads in mind.items():
        for p in payloads:
            top_payloads[p] += 1

    console.print("\n[bold cyan]Top Payload-i iz ShadowMind baze:[/bold cyan]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Payload")
    table.add_column("Pojavljivanja", justify="right")
    for payload, count in top_payloads.most_common(10):
        table.add_row(payload[:40], str(count))
    console.print(table)

def analyze_signatures():
    if not os.path.exists(SIG_PATH):
        return

    with open(SIG_PATH, "r") as f:
        data = json.load(f)

    console.print("\n[bold green]Najuspešniji profili po metama:[/bold green]")
    table = Table(show_header=True, header_style="bold yellow")
    table.add_column("Host")
    table.add_column("Broj hitova")
    table.add_column("Najčešći profil")

    for host, entries in data.items():
        profiles = [e["profile"] for e in entries]
        counter = Counter(profiles)
        top = counter.most_common(1)[0]
        table.add_row(host, str(len(entries)), top[0])

    console.print(table)

if __name__ == "__main__":
    analyze_shadowbrain()
    analyze_signatures()
