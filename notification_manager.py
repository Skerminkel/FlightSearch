import os
from dotenv import load_dotenv
from twilio.rest import Client


class NotificationManager:

    def __init__(self, data_in: dict):
        load_dotenv("C:/env/.env.txt")
        self.account_sid = os.getenv("account_sid")
        self.auth_token = os.getenv("auth_token")

        self.price = data_in["price"]
        self.departure_city = data_in["cityFrom"]
        self.departure_code = data_in["cityCodeFrom"]
        departure_time = data_in["route"][0]["local_departure"]
        self.dep_date = departure_time.split("T")[0]
        self.dep_time = departure_time.split("T")[1].split(".")[0]

        self.arrival_city = data_in["cityTo"]
        self.arrival_code = data_in["cityCodeTo"]
        arrival_time = data_in["route"][0]["local_arrival"]
        self.arr_date = arrival_time.split("T")[0]
        self.arr_time = arrival_time.split("T")[1].split(".")[0]

    def send_message(self):

        body = f"Cheap ticket alert! {self.price} to fly " \
               f"{self.departure_city}|{self.departure_code} > {self.arrival_city}|{self.arrival_code}\n"\
               f"Leaves: {self.dep_date} at {self.dep_time}. \nArrives: {self.arr_date} at {self.arr_time} "

        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=body, from_='+13865165795',
            to='+27711472103')

        print("message sent")