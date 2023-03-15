import requests

url = "https://catfact.ninja/facts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    fact = data['data'][0]['fact']
    print(fact)
else:
    print("Failed to get cat fact. Error code:", response.status_code)