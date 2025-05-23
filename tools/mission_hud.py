from rich.live import Live
from rich.table import Table
from rich.console import Console
import time
import json
import os

LOG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs", "live_log.txt"))

console = Console()

def read_last_lines(path, limit=10):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        lines = f.readlines()
    return lines[-limit:]

def render():
    table = Table(title="ShadowFox Mission HUD")

    table.add_column("TIME", style="dim", width=20)
    table.add_column("EVENT", style="cyan")

    lines = read_last_lines(LOG_PATH)
    for line in lines:
        if "]" in line:
            time_part = line.split("]")[0].strip("[")
            event = line.split("]")[1].strip()
            table.add_row(time_part, event)
    return table

def main():
    last_seen = ""
    idle_counter = 0
    with Live(render(), refresh_per_second=2) as live:
        while True:
            time.sleep(1)
            current = read_last_lines(LOG_PATH)
            if current and current[-1] != last_seen:
                last_seen = current[-1]
                idle_counter = 0
            else:
                idle_counter += 1

            if idle_counter >= 10:  # 10 sekundi bez novih logova
                print("\n[MISIJIA] HUD zatvara - nema novih događaja.")
                break

            live.update(render())
if __name__ == "__main__":
    main()
