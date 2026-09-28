import requests
responce = requests.get("https://api.github.com")
print(responce.status_code)
