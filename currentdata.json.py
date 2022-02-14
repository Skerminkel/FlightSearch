current_data = {
    "prices": [
        {
            "city": "Paris",
            "iataCode": "CDG",
            "lowestPrice": 54,
            "id": 2
        },
        {
            "city": "Berlin",
            "iataCode": "SXF",
            "lowestPrice": 42,
            "id": 3
        },
        {
            "city": "Tokyo",
            "iataCode": "HND",
            "lowestPrice": 485,
            "id": 4
        },
        {
            "city": "Sydney",
            "iataCode": "SYD",
            "lowestPrice": 551,
            "id": 5
        },
        {
            "city": "Istanbul",
            "iataCode": "IST",
            "lowestPrice": 95,
            "id": 6
        },
        {
            "city": "Kuala Lumpur",
            "iataCode": "KUL",
            "lowestPrice": 414,
            "id": 7
        },
        {
            "city": "New York",
            "iataCode": "JFK",
            "lowestPrice": 240,
            "id": 8
        },
        {
            "city": "San Francisco",
            "iataCode": "SAF",
            "lowestPrice": 260,
            "id": 9
        },
        {
            "city": "Cape Town",
            "iataCode": "CPT",
            "lowestPrice": 378,
            "id": 10
        },
        {
            "city": "Prague",
            "iataCode": "PRG",
            "lowestPrice": 772,
            "id": 11
        }
    ]
}

for entry in current_data["prices"]:
    print(entry["city"])