import os
from rich.console import Console
from rich.table import Table

REPORT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports"))

def list_reports():
    files = os.listdir(REPORT_DIR)
    pdfs = [f for f in files if f.endswith(".pdf")]

    console = Console()
    table = Table(title="ShadowFox11 Izveštaji", show_lines=True)

    table.add_column("Br", style="cyan", no_wrap=True)
    table.add_column("Naziv", style="green")
    table.add_column("Veličina (KB)", style="magenta")

    for idx, name in enumerate(pdfs, 1):
        path = os.path.join(REPORT_DIR, name)
        size_kb = os.path.getsize(path) // 1024
        table.add_row(str(idx), name, str(size_kb))

    if not pdfs:
        console.print("[!] Nema izveštaja.")
    else:
        console.print(table)

if __name__ == "__main__":
    list_reports()
