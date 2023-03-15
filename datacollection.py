import requests
import json
import time
from datetime import datetime
#import urllib3
#import urllib.parse

class Tram:
    def __init__(self, line, arrival_time, richtung):
        self.line = line
        self.arrival_time = arrival_time
        self.richtung = richtung

    def __eq__(self, other): 
        if not isinstance(other, Tram):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.line == other.line and self.line == other.line and self.arrival_time == other.arrival_time   


def is_relevant(leg):
    #print(leg['type'])
    if 'type' not in leg:
        return False
    elif leg['type'] == ('walk' or 'bike'):
        #print('returned false for walk')
        return False
    elif leg['name'] != 'Zürich, Winzerstrasse' and leg['name'] != 'Zürich, Winzerstrasse Süd':
        #print(leg['name'] + ' not accepted')
        return False
    #print(leg['name'])
    return True

def SaveDataInList(departs):

    #departs = datacollection.get_departs()
    next_departures = []

    for i in range(len(departs['results'])):
        
        for j in range(len(departs['results'][i]['connections'])):
            #print(departs['results'][i]['connections'][j]["legs"][0]['departure'])
            k = 0
            while 'departure' in departs['results'][i]['connections'][j]["legs"][k]:

                if is_relevant(departs['results'][i]['connections'][j]['legs'][k]):
                    
                    current_tram = Tram(departs['results'][i]['connections'][j]['legs'][k]['line'], datetime.strptime(departs['results'][i]['connections'][j]['legs'][k]['departure'], '%Y-%m-%d %X'), departs['results'][i]['connections'][j]['legs'][k]['terminal'])
                    next_departures.append(current_tram)   
                
                k += 1
    return next_departures

def get_departs(departure_location):

    url = "https://timetable.search.ch/api/route.json?from=" + departure_location + "&to[0]=Z%C3%BCrich+HB&to[1]=Z%C3%BCrich%2C+Meierhofplatz&to[2]=Z%C3%BCrich+Altstetten&one_to_many=1"
    #url_root = "https://timetable.search.ch/api/route.json?"
    #url = url_root + encoded_data
    #print(url)
    #http = urllib3.PoolManager()
    #response = http.request(
    #    'GET',
    #    url,
    #    fields= = {
    #    'from' : 'Bern',
    #    'to' : {
    #        '0' : 'Luzern'    
    #        },
    #    'one_to_many' : '1'
    #    })

    response = requests.get(url)
    #print(response)


    if response.status_code == 200:
        data = response.json()
        #print(fact)


        #json_object = json.loads(data)

        json_formatted_str = json.dumps(data, indent=2)

        #print(json_formatted_str)
        with open('json_data.json', 'w') as outfile:
            outfile.write(json_formatted_str)
    
        return(data)

    else:
        print("Failed to get connections. Error code:", response.status_code)

if __name__ == "__main__":
    stationboard = get_departs()
    