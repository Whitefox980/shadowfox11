from modules.center_loader import load_center_data, get_headers, get_payloads, get_targets

data = load_center_data()

for domain, props in get_targets(data).items():
    headers = get_headers(data, domain)
    payloads = get_payloads(data, props["type"])
    print(f"[{domain}]")
    print(" Headers:", headers)
    print(" Payloads:", payloads)
    print()
