from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(url, valid_hits, path="reports/"):
    file_path = f"{path}report_{url.replace('://', '_').replace('/', '_')}.pdf"
    c = canvas.Canvas(file_path, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, f"ShadowFox Report for: {url}")
    y = 760
    for hit in valid_hits:
        c.drawString(100, y, f"- {hit}")
        y -= 20
    c.save()
    print(f"[PDF] Izveštaj snimljen: {file_path}")
