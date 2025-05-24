# tools/gen_targets.py

default_params = ["q", "input", "query", "term", "page", "s", "keyword", "id", "username"]
base_urls = [
    "https://kayak.ai",
    "https://www.hotelscombined.com",
    "https://www.checkfelix.com/search"
]

with open("targets.txt", "w") as f:
    for url in base_urls:
        for param in default_params:
            full_url = f"{url}?{param}=FUZZ"
            f.write(f"{full_url},xss,2\n")

print("[✓] Generisani targets ubačeni u targets.txt")
