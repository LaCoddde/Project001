import requests

request = requests.get("https://nottheking.pythonanywhere.com/")
data = request.json()

print(data)
