import threading
import requests
import time

urls = [
    "https://api.github.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts"
]

def fetch(url):
    print(f"Fetching {url}")
    response = requests.get(url)
    print(f"Done {url} → Status: {response.status_code}")

threads = []
start = time.time()

for url in urls:
    t = threading.Thread(target=fetch, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()

print("Time taken:", end - start)