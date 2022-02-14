import os
from dotenv import load_dotenv
import datetime as dt
import requests
from notification_manager import NotificationManager as nm


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API (Tequila/Kiwi).
    Contains relevant data on flight statistics.
    """

    def __init__(self, fly_to: str, fly_from: str = "JNB", search_len: int = 30):
        """
        :param fly_to: str: destination. Required.
        :param fly_from: str: optional, defaults to RSA
        :param search_len: int: optional, defaults to 30
        """
        load_dotenv("/env/.env.txt")
        self.api_key = os.getenv("api_key_tequila")
        self.search_len = search_len
        self.endpoint = "http://tequila-api.kiwi.com/v2/search"
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.dates = {}

        if len(self.dates) == 0:
            self.set_dates()

        self.header = {"apikey": self.api_key}
        """
        For some godforsaken reason, even though in their documentation fly_from is listed before fly_to,
        you HAVE to have fly_to listed first in params or it will give you an error. -_-
        """
        self.parameters = {
            "fly_to": self.fly_to,  # str destination location
            "fly_from": self.fly_from,  # str start location
            "date_from": self.dates["date_from"],  # dd/mm/YYYY search from this date
            "date_to": self.dates["date_to"],  # dd/mm/YYYY search up to this date
        }

    def set_dates(self):
        date_from = dt.datetime.today().strftime("%d/%m/%Y")
        date_to = (dt.date.today() + dt.timedelta(days=self.search_len)).strftime("%d/%m/%Y")

        self.dates["date_from"] = date_from
        self.dates["date_to"] = date_to

    def api_call(self, lowest):
        best_deal = None
        response = requests.get(url=self.endpoint, headers=self.header, params=self.parameters).json()
        # compared = response["data"][:2]
        # for compare in compared:
        #     if compare["price"] < lowest:
        #         print("sending message")
        #         lowest = compare["price"]
        #         best_deal = {compare["price"]: compare["local_departure"]}
        #         # nm(compare).send_message()
        # return best_deal
        print(response)

FlightSearch("BWU", "JNB", 30).api_call(2000)