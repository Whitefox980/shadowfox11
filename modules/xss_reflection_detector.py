import requests

def is_reflected_xss(url, payload="SHADOWXSS123"):
    try:
        test_url = url.replace("FUZZ", payload)
        r = requests.get(test_url, timeout=5)
        return payload in r.text
    except Exception as e:
        return False
