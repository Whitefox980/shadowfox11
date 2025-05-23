import os
from rich.console import Console
from rich.table import Table

REPORT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports"))

def search_reports(query):
    files = os.listdir(REPORT_DIR)
    pdfs = [f for f in files if f.endswith(".pdf") and query.lower() in f.lower()]

    console = Console()
    table = Table(title=f"Rezultati za: '{query}'")

    table.add_column("Naziv fajla", style="green")
    table.add_column("Veličina (KB)", style="magenta")

    if not pdfs:
        console.print(f"[!] Nema rezultata za: '{query}'")
        return

    for name in pdfs:
        size = os.path.getsize(os.path.join(REPORT_DIR, name)) // 1024
        table.add_row(name, str(size))

    console.print(table)

if __name__ == "__main__":
    query = input("Unesi ključnu reč za pretragu izveštaja: ")
    search_reports(query)
