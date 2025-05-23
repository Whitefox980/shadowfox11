def generate_replay_summary(url, payloads, result_file="reports/replay.md"):
    with open(result_file, "w") as f:
        f.write(f"# Replay Report for {url}\n\n")
        for p in payloads:
            f.write(f"- {p}\n")
    print(f"[REPLAY] Zapisano u: {result_file}")
