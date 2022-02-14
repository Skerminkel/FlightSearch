import requests
import os
from dotenv import load_dotenv


class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """

    # TODO: add sheety API details
    def __init__(self):
        load_dotenv("/env/.env.txt")
        self.apikey = os.getenv("api_key_sheety")
        self.header = {
            "Authorization": self.apikey
        }
        self.endpoint = "https://api.sheety.co/f0ec68e3a1dd6ccd89be3a91e6d4c158/flightDeals/prices"

    def get_current(self):
        current_data = requests.get(self.endpoint, headers=self.header).json()
        return current_data

    def update_new(self, data_in: list):

        for entry in data_in:

            row = entry[0]
            data = entry[1]
            price = [key for key in data][0]
            departure = data[price]
            date = departure.split("T")[0]
            time = departure.split("T")[1].split(".")[0]

            new_data = {
                "price": {
                     "lowestPrice": price,
                     "departure": date,
                     "time": time,
                     }
            }

            update = requests.put(url=f"{self.endpoint}/{row}", json=new_data, headers=self.header)
            update.raise_for_status()
            print(update.text)
