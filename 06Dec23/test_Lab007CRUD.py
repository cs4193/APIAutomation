import requests
import pytest
import Lab006AuthPost


def test_PUT_method():
    cookie_value = "token=" + Lab006AuthPost.generate_token()
    booking_id = str(Lab006AuthPost.create_booking())
    Headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookie_value}
    URL = "https://restful-booker.herokuapp.com/booking/" + booking_id
    json_payload = {
                    "firstname" : "Chetan",
                    "lastname" : "Brown",
                    "totalprice" : 111,
                    "depositpaid" : True,
                    "bookingdates" : {
                        "checkin" : "2023-01-01",
                        "checkout" : "2024-01-01"
                    },
                    "additionalneeds" : "Breakfast"
                }
    response = requests.put(url=URL, headers=Headers, json=json_payload )
    assert response.status_code == 200


def test_PATCH_method():

    cookie_value = "token=" + Lab006AuthPost.generate_token()
    booking_id = str(Lab006AuthPost.create_booking())
    Headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookie_value}
    URL = "https://restful-booker.herokuapp.com/booking/" + booking_id
    json_payload = {
        "firstname": "Chetan",
        "lastname": "Brown"
    }
    response = requests.patch(url=URL, headers=Headers, json=json_payload)
    assert response.status_code == 200


def test_Delete_method():
    cookie_value = "token=" + Lab006AuthPost.generate_token()
    booking_id = str(Lab006AuthPost.create_booking())
    Headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookie_value}
    URL = "https://restful-booker.herokuapp.com/booking/" + booking_id
    response = requests.delete(url=URL, headers=Headers)
    assert response.status_code == 201

