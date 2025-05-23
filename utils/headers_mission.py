def build_mission_headers(profile_headers, agent_name="Whitefox980"):
    mission_headers = {
        "User-Agent": "ShadowFox/1.1",
        "X-ShadowFox-Agent": agent_name,
        "X-Permission-Level": "probe",
        "X-Mission-Scope": "recon+mutate",
        "X-Support-Platform": "HackerOne",
    }
    # Kombinuj sve zaglavlja
    combined = {**profile_headers, **mission_headers}
    return combined
