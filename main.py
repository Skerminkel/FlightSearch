from flight_search import FlightSearch as fs
from data_manager import DataManager as dm

sheet = dm()
to_change = []

for entry in sheet.get_current()["prices"]:
    lowest = entry["lowestPrice"]
    flight = fs(entry["iataCode"])
    target = flight.api_call(lowest)
    if target is not None:
        to_change.append([entry["id"], target])

if len(to_change) > 1:
    print("No luck")
else:
    print(to_change)

sheet.update_new(to_change)

#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.