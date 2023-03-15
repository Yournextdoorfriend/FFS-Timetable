import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    fact = data
    print(fact)
else:
    print("Failed to get cat fact. Error code:", response.status_code)