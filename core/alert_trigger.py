import os
import datetime

ALERT_LOG = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs", "alerts.txt"))

def trigger_alert(payload, score, url):
    alert_msg = f"[ALERT] {datetime.datetime.now().isoformat()} :: SCORE {score} :: {url} :: {payload}"
    print(f"\n\033[1;31m{alert_msg}\033[0m")  # crveni terminal output
    with open(ALERT_LOG, "a") as f:
        f.write(alert_msg + "\n")

    # opcionalno: oglasiti zvuk (ako želiš i koristiš play-audio)
    # os.system("play /usr/share/sounds/alert.wav")

def read_alert_log():
    if not os.path.exists(ALERT_LOG):
        print("[ALERT] Nema prethodnih alarma.")
        return
    with open(ALERT_LOG, "r") as f:
        for line in f:
            print(line.strip())
