from rich.live import Live
from rich.table import Table
from rich.console import Console
from rich.progress import BarColumn, Progress
import time
import os
import re

LOG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs", "live_log.txt"))

def extract_payload_scores():
    scores = []
    if not os.path.exists(LOG_PATH):
        return scores

    with open(LOG_PATH, "r") as f:
        for line in f:
            match = re.search(r"SCORE (\d+) (.+)", line)
            if match:
                score = int(match.group(1))
                payload = match.group(2).strip()
                scores.append((payload, score))
    return scores[-10:]  # poslednjih 10

def render():
    scores = extract_payload_scores()
    table = Table(title="ShadowFox Payload Score Chart")

    table.add_column("Payload", style="bold cyan", overflow="fold")
    table.add_column("Score", style="green")
    table.add_column("Visual", style="magenta")

    for payload, score in scores:
        bar = "█" * (score // 10)
        table.add_row(payload[:40], str(score), bar)

    return table

def main():
    with Live(render(), refresh_per_second=1) as live:
        idle = 0
        last_state = ""
        while True:
            time.sleep(1)
            state = str(extract_payload_scores())
            if state != last_state:
                idle = 0
                last_state = state
            else:
                idle += 1
            if idle >= 15:
                print("\n[HUD] Automatsko gašenje - nema novih payload-a.")
                break
            live.update(render())

if __name__ == "__main__":
    main()
