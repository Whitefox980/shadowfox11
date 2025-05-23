from rich.console import Console
from rich.table import Table
import os
import json

MIND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "shadow_mind.json"))

def draw_payload_map():
    with open(MIND_PATH, "r") as f:
        data = json.load(f)

    console = Console()
    table = Table(title="ShadowMind Payload Map")

    table.add_column("Vektor", style="cyan", no_wrap=True)
    table.add_column("Broj pogodaka", style="green")
    table.add_column("Top primer", style="magenta")

    for vector, payloads in data.items():
        count = str(len(payloads))
        sample = payloads[0] if payloads else "-"
        table.add_row(vector, count, sample)

    console.print(table)

if __name__ == "__main__":
    draw_payload_map()
