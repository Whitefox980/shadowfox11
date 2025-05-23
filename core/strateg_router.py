import datetime
from urllib.parse import urlparse

def choose_vector(url):
    domain = urlparse(url).netloc.lower()
    hour = datetime.datetime.now().hour

    if "admin" in url or "login" in url:
        return "sqli"
    elif "search" in url or "query" in url:
        return "xss"
    elif hour < 6:
        return "lfi"
    else:
        return "xss"
