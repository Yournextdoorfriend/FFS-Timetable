import datacollection
import datareordering
from datetime import datetime
import json
import time

if __name__ == "__main__":

    departs_1 = datacollection.get_departs("Z%C3%BCrich%2C+Winzerstrasse")
    departs_2 = datacollection.get_departs("Z%C3%BCrich%2C+Winzerstrasse+S\u00fcd")

    next_departures = datacollection.SaveDataInList(departs_1) + datacollection.SaveDataInList(departs_2)

    datareordering.bubbleSort(next_departures)

    next_departures = datareordering.trashDuplicates(next_departures)

    for i, tram in enumerate(next_departures):
       print(next_departures[i].line + ' towards ' + next_departures[i].richtung + ' at ' + datetime.strftime(next_departures[i].arrival_time, '%x   %X'))

    