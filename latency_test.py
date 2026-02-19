import requests

urls = ["https://google.com", "https://github.com", "https://open-meteo.com"]

for url in urls:
    try:
        r = requests.get(url, timeout=5)
        print(f"{url} responded in {r.elapsed.total_seconds()} seconds")
    except requests.exceptions.RequestException:
        print(f"{url} is unreachable")
