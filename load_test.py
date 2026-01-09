import requests
from concurrent.futures import ThreadPoolExecutor

URL = "http://127.0.0.1:8000/"

def hit_api():
    try:
        r = requests.get(URL, timeout=2)
        return r.status_code
    except:
        return "ERR"

with ThreadPoolExecutor(max_workers=1000) as executor:
    results = list(executor.map(lambda _: hit_api(), range(20)))

print("200 OK:", results.count(200))
print("429:", results.count(429))
