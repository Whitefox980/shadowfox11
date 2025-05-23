import json
import os
import datetime

QUEUE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "task_queue.json"))

def init_queue():
    if not os.path.exists(QUEUE_PATH):
        with open(QUEUE_PATH, "w") as f:
            json.dump([], f)

def add_task(url, priority=1, vector="xss"):
    init_queue()

    # Učitaj postojeće zadatke
    with open(QUEUE_PATH, "r") as f:
        try:
            data = json.load(f)
        except:
            data = []

    task = {
        "url": url,
        "vector": vector,
        "priority": priority,
        "created": datetime.datetime.now().isoformat()
    }

    data.append(task)

    # Upis u fajl
    with open(QUEUE_PATH, "w") as f:
        json.dump(sorted(data, key=lambda x: x["priority"]), f, indent=4)

    print(f"[DEBUG] Dodato u fajl: {len(data)} taskova")
def get_next_task():
    init_queue()
    with open(QUEUE_PATH, "r") as f:
        data = json.load(f)

    print(f"[DEBUG] Učitao queue sa {len(data)} zadatka:")
    for d in data:
        print(f" - {d['url']} | {d['vector']} | prio {d['priority']}")

    if not data or len(data) == 0:
        return None

    task = data.pop(0)
    return task, data
def save_queue(data):
    with open(QUEUE_PATH, "w") as f:
        json.dump(data, f, indent=4)
