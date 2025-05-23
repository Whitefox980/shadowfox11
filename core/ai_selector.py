import datetime

def select_vector_by_time():
    hour = datetime.datetime.now().hour
    if 0 <= hour <= 6:
        return "sqli"
    elif 7 <= hour <= 17:
        return "xss"
    else:
        return "lfi"
