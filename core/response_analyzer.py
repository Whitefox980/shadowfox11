def analyze_response(response, payload):
    score = 0
    if payload in response.text:
        score += 50
    if response.status_code == 200:
        score += 10
    if "alert" in response.text or "confirm" in response.text:
        score += 30
    return score
