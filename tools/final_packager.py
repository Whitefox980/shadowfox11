import os
import zipfile
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORT_DIR = os.path.join(BASE_DIR, "reports")
LOG_DIR = os.path.join(BASE_DIR, "logs", "snapshots")
EXPORT_PATH = os.path.join(BASE_DIR, "exports")

def package_case():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    zip_name = f"shadowfox_case_{timestamp}.zip"
    zip_path = os.path.join(EXPORT_PATH, zip_name)

    if not os.path.exists(EXPORT_PATH):
        os.makedirs(EXPORT_PATH)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Dodaj PDF izveštaje
        for f in os.listdir(REPORT_DIR):
            if f.endswith(".pdf") or f.endswith(".txt"):
                zipf.write(os.path.join(REPORT_DIR, f), f"reports/{f}")
        # Dodaj live log
        log_file = os.path.join(LOG_DIR, "live_log.txt")
        if os.path.exists(log_file):
            zipf.write(log_file, "logs/live_log.txt")

    print(f"[✓] Paket spreman: {zip_path}")

if __name__ == "__main__":
    package_case()
