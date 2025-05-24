import json
from datetime import datetime

def generate_html_report(result_data, filename="reports/replay.html"):
    with open(filename, "w") as f:
        f.write("<html><head><title>ShadowFox Report</title><style>")
        f.write("body { font-family: monospace; background: #111; color: #0f0; padding: 20px; }")
        f.write("pre { background: #222; padding: 10px; border-left: 3px solid #0f0; }")
        f.write("</style></head><body>")
        f.write("<h1>ShadowFox :: Attack Report</h1>")

        for entry in result_data:
            f.write(f"<h3>{entry['url']}</h3>")
            f.write(f"<b>Vector:</b> {entry['vector']}<br>")
            f.write(f"<b>Payload:</b> <code>{entry['payload']}</code><br>")
            f.write(f"<b>Status:</b> {entry['status']} | <b>Size:</b> {entry['size']} B<br>")
            f.write("<pre>")
            f.write(entry['response'][:1000])  # truncate for safety
            f.write("</pre><hr>")

        f.write("</body></html>")
