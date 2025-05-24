import os
import hashlib
from datetime import datetime

def generate_html_report(payload, target_url, profile, vector, score):
    folder = "reports/html"
    os.makedirs(folder, exist_ok=True)

    report_hash = hashlib.sha256(f"{target_url}{payload}{datetime.now()}".encode()).hexdigest()[:10]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""
    <html>
    <head><title>ShadowFox AI Report</title></head>
    <body style='font-family:monospace; background:#0d0d0d; color:#00ff99; padding:20px'>
        <h2>ShadowFox-X AI HIT REPORT</h2>
        <p><b>Target:</b> {target_url}</p>
        <p><b>Payload:</b> {payload}</p>
        <p><b>Vector:</b> {vector}</p>
        <p><b>Agent:</b> {profile}</p>
        <p><b>Score:</b> {score}</p>
        <p><b>Timestamp:</b> {timestamp}</p>
        <hr>
        <h3>AI Analysis:</h3>
        <p>This payload was likely reflected in the HTML response, suggesting a potential <b>{vector.upper()}</b> vulnerability. Manual validation is recommended.</p>
        <p><b>Recommended fix:</b> Sanitize user input, encode output, and implement strict CSP.</p>
        <hr>
        <p><i>Report ID:</i> {report_hash}</p>
        <p><i>ShadowFox-X AI</i></p>
    </body>
    </html>
    """

    with open(f"{folder}/hit_{report_hash}.html", "w") as f:
        f.write(html)
