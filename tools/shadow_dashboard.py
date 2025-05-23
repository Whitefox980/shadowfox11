from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os
import json

def get_queue_status():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "task_queue.json"))
    if not os.path.exists(path):
        return 0
    with open(path, "r") as f:
        data = json.load(f)
        return len(data)

def get_mind_stats():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "shadow_mind.json"))
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def show_dashboard():
    console = Console()
    queue_count = get_queue_status()
    mind_data = get_mind_stats()

    console.rule("[bold green]ShadowFox11 :: Dashboard")

    console.print(Panel(f"[cyan]Zadaci u redu čekanja:[/] [bold yellow]{queue_count}[/]"))

    table = Table(title="ShadowMind Statistika")
    table.add_column("Vektor", style="magenta")
    table.add_column("Pogodaka", style="green")
    table.add_column("Primer payload", style="white")

    for vector, payloads in mind_data.items():
        table.add_row(vector, str(len(payloads)), payloads[0] if payloads else "-")

    console.print(table)

if __name__ == "__main__":
    show_dashboard()
