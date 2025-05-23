from fpdf import FPDF

def generate_pdf(url, payload, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="ShadowFox Vulnerability Report", ln=True)
    pdf.cell(200, 10, txt=f"URL: {url}", ln=True)
    pdf.cell(200, 10, txt=f"Payload: {payload}", ln=True)
    pdf.output(f"reports/{filename}")
