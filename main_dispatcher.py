from agents.ghost_agent import run_ghost_crawl
from agents.observer_agent import simulate_user_behavior
from agents.exfiltrator import export_detections_to_json
from scripts.pdf_report_maker import generate_pdf_report
from utils.live_logger import log_line
from core_loader import get_attack_profile

# Simulacija jedne ShadowFox misije
def run_full_mission():
    log_line("=== ShadowFox11 MISSION START ===")
    profile = get_attack_profile("DefaultHuman")

    # Stealth recon
    run_ghost_crawl()
    log_line("GhostCrawl završio.")

    # Simulacija ponašanja
    simulate_user_behavior(profile)
    log_line("Ponašanje simulirano.")

    # Eksport detekcija
    export_detections_to_json()
    log_line("Detekcije izvezene.")

    # Dummy report (test primer)
    generate_pdf_report("http://dummy.url", ["<script>x</script>", "' OR 1=1"], "reports/")
    log_line("PDF izveštaj generisan.")

    log_line("=== ShadowFox11 MISSION END ===")

if __name__ == "__main__":
    run_full_mission()
