import os
import sys
import time
import subprocess

def clear():
    os.system("clear")

def header():
    print("="*40)
    print("    SHADOWFOX AI MISSION CENTER")
    print("="*40)

def menu():
    header()
    print("1. Pokreni AUTO MODE napad")
    print("2. Učitaj mete iz targets.txt")
    print("3. Pogledaj zadnje AI pogodke")
    print("4. Pogledaj targets.txt")
    print("5. Otvori izveštaje")
    print("6. Izađi")
    print("="*40)

def start_auto_mode():
    print("[+] Pokrećem AUTO MODE...")
    os.system("python3 main/auto_mode.py")
    input("\n[Pritisni Enter za povratak u meni]")

def load_targets():
    print("[+] Učitavam mete iz targets.txt...")
    os.system("python3 tools/load_targets.py")
    input("\n[Pritisni Enter za povratak u meni]")

def show_hits():
    print("[+] Pregled AI pogodaka...")
    os.system("python3 tools/shadowbrain_replay.py")
    input("\n[Pritisni Enter za povratak u meni]")

def open_targets_txt():
    print("[+] Otvaram targets.txt...")
    os.system("nano targets.txt")

def open_reports():
    print("[+] Otvaram folder sa PDF izveštajima...")
    os.system("ls -lt reports/")
    input("\n[Pritisni Enter za povratak u meni]")

def main():
    while True:
        clear()
        menu()
        choice = input("Izaberi opciju: ")

        if choice == "1":
            start_auto_mode()
        elif choice == "2":
            load_targets()
        elif choice == "3":
            show_hits()
        elif choice == "4":
            open_targets_txt()
        elif choice == "5":
            open_reports()
        elif choice == "6":
            print("[*] Izlazim.")
            sys.exit()
        else:
            print("[!] Pogrešan izbor.")
            time.sleep(1)

if __name__ == "__main__":
    main()
