import datetime

def log_line(message, logfile="logs/snapshots/live_log.txt"):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as f:
        f.write(f"[{now}] {message}\n")
