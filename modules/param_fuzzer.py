import requests

common_params = ["q", "search", "query", "id", "input", "term", "page", "s", "keyword", "username"]
test_payload = "SHADOWFOX_TEST_1337"

def find_fuzzable_param(base_url):
    candidates = []
    for param in common_params:
        test_url = f"{base_url}?{param}={test_payload}"
        try:
            r = requests.get(test_url, timeout=5)
            if test_payload in r.text:
                candidates.append(param)
        except:
            continue
    return candidates
# modules/param_fuzzer.py

