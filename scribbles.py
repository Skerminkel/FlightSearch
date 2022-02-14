from dotenv import load_dotenv
import os
import requests

load_dotenv("/env/.env.txt")
apikey = os.getenv("api_key_sheety")
header = {
    "Authorization": apikey
}
endpoint = "https://api.sheety.co/f0ec68e3a1dd6ccd89be3a91e6d4c158/flightDeals/prices/2"

# new = {
#     "price": [
#         {
#             "lowestPrice": 900
#         }
#     ]
# }

new_data = {
    "price": {
        "iataCode": "test"
    }
}
response = requests.put(
    url=f"{endpoint}",
    json=new_data,
    headers=header
)
print(response.text)

# update = requests.put(endpoint, headers=header, json=new)
# print(update.text)