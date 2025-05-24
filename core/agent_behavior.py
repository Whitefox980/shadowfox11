import time
import random
from rich.console import Console
console = Console()

def simulate_behavior(mode="default"):
    if mode == "curious_clicker":
        _curious_clicker()
    elif mode == "lazy_browser":
        _lazy_browser()
    elif mode == "paranoid_lurker":
        _paranoid_lurker()
    elif mode == "distracted_user":
        _distracted_user()
    else:
        _default_behavior()

def _curious_clicker():
    console.print("[BEHAVIOR] Clicking, typing, exploring...", style="cyan")
    time.sleep(random.uniform(1.5, 3.0))
    _fake_typing()
    time.sleep(random.uniform(1.0, 2.5))
    _mouse_spin()

def _lazy_browser():
    console.print("[BEHAVIOR] Staring at screen 6s...", style="yellow")
    time.sleep(random.uniform(5.5, 7.5))

def _paranoid_lurker():
    console.print("[BEHAVIOR] Lurking silently 10-15s...", style="red")
    time.sleep(random.uniform(10.0, 15.0))

def _distracted_user():
    console.print("[BEHAVIOR] Switched tab... comes back...", style="magenta")
    time.sleep(random.uniform(8.0, 12.0))
    _fake_typing()

def _default_behavior():
    console.print("[BEHAVIOR] Just observing...", style="white")
    time.sleep(random.uniform(2.0, 3.5))

def _fake_typing():
    console.print("  *User typing...*", style="dim")
    time.sleep(random.uniform(1.0, 2.0))

def _mouse_spin():
    console.print("  *Mouse spins in a circle...*", style="dim")
    time.sleep(random.uniform(0.8, 1.5))
