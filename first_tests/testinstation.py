import requests
import json

url = "https://timetable.search.ch/api/station.json?stop=Z%C3%BCrich,+Winzerstrasse"
response = requests.get(url)

#%FC
#https://timetable.search.ch/api/route.json?from=Einsiedeln&to=Z%C3%BCrich,+F%C3%B6rrlibuckstr.+60

if response.status_code == 200:
    data = response.json()
    fact = data
    #print(fact)


    #json_object = json.loads(data)

    json_formatted_str = json.dumps(data, indent=2)

    print(json_formatted_str)

else:
    print("Failed to get cat fact. Error code:", response.status_code)