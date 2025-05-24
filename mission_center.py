elif choice == "5":
    print("\n[+] Otvaram folder sa izveštajima...\n")
    reports_path = "reports"
    if not os.path.exists(reports_path):
        print("[X] Folder 'reports' ne postoji.")
        input("\n[Pritisni Enter za povratak u meni]")
        continue

    files = os.listdir(reports_path)
    files = sorted([f for f in files if f.endswith((".txt", ".json", ".pdf"))])
    if not files:
        print("[X] Nema izveštaja.")
        input("\n[Pritisni Enter za povratak u meni]")
        continue

    for idx, file in enumerate(files, 1):
        path = os.path.join(reports_path, file)
        try:
            summary = ""
            if file.endswith(".json"):
                with open(path, "r") as f:
                    data = json.load(f)
                    vector = data.get("vector", "N/A")
                    hits = data.get("hits", 1)
                    summary = f"{hits} pogodaka | Vektor: {vector}"
            elif file.endswith(".txt"):
                with open(path, "r") as f:
                    lines = f.readlines()
                    summary = f"{len(lines)} linija teksta"
            elif file.endswith(".pdf"):
                summary = "PDF izveštaj (nije analiziran)"
        except:
            summary = "Greška pri čitanju"

        print(f"{idx}. {file.ljust(35)} | {summary}")

    print("\n[Izaberi broj da vidiš sadržaj fajla ili Enter za povratak]")
    sub_choice = input(">> ")

    if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(files):
        file_path = os.path.join(reports_path, files[int(sub_choice) - 1])
        print(f"\n[+] Sadržaj: {file_path}\n")
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            print(f.read()[:3000])  # limit prikaza
        print("\n--- kraj sadržaja ---")
        input("[Enter za nazad u meni]")
    os.system(f"termux-open {file_path}")
