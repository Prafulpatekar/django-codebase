import requests

ENDPOINT = "http://localhost:8000"

res = requests.get(ENDPOINT)
print(res.json())
print(res.status_code)
