import requests
import pytest


def generate_token():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers_auth = {"Content-Type":"application/json"}
    payload_auth = {
                    "username" : "admin",
                    "password" : "password123"
                    }
    response = requests.post(url=URL,headers=headers_auth,json=payload_auth)
    data = response.json()
    print(data["token"])
    return data["token"]


def create_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 200

    data = response.json()
    booking_id = data["bookingid"]
    assert data["bookingid"] is not None
    print(booking_id)
    return booking_id

print(generate_token())
print(create_booking())

