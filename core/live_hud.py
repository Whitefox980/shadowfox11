from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.console import Console
import time

console = Console()

status = {
    "meta": "-",
    "vector": "-",
    "agent": "-",
    "payload": "-",
    "response": "-",
    "result": "-",
    "state": "Initializing"
}

def update_status(**kwargs):
    for k, v in kwargs.items():
        status[k] = v

def render_hud():
    table = Table.grid(padding=1)
    table.add_row(f"[bold cyan]Meta:[/bold cyan] {status['meta']}", f"[bold cyan]Vector:[/bold cyan] {status['vector']}")
    table.add_row(f"[bold magenta]Agent:[/bold magenta] {status['agent']}", f"[bold magenta]State:[/bold magenta] {status['state']}")
    table.add_row(f"[bold yellow]Payload:[/bold yellow] {status['payload']}")
    table.add_row(f"[bold green]Response:[/bold green] {status['response']}", f"[bold green]Result:[/bold green] {status['result']}")
    return Panel(table, title="SHADOWFOX :: LIVE HUD", border_style="bright_blue")

def live_loop():
    with Live(render_hud(), refresh_per_second=4) as live:
        while True:
            time.sleep(0.5)
            live.update(render_hud())
