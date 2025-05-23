
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.xss_reflection_detector import is_reflected_xss

# ZAMENI OVU URL sa nekom test metom koja reflektuje
url = "https://www.hotelscombined.com/search?q=FUZZ"

if is_reflected_xss(url):
    print("[✓] Refleksija DETEKTOVANA!")
else:
    print("[X] Refleksija NIJE pronađena.")
