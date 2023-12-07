# how to create booking using Pytest
# requirements
# url,headers,body(payload),TOken/Auth,verify booking ID


import requests
import pytest


@pytest.mark.positive
def test_create_booking():
    print("Create booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers ={"Content-Type":"application/json"}
    json_payload = {
                        "firstname" : "Jim",
                        "lastname" : "Brown",
                        "totalprice" : 111,
                        "depositpaid" : True,
                        "bookingdates" : {
                            "checkin" : "2018-01-01",
                            "checkout" : "2019-01-01"
                        },
                        "additionalneeds" : "Breakfast"
                    }
    print(type(headers))
    print(type(json_payload))
    response = requests.post(url=URL,headers=headers,json=json_payload)
    assert response.status_code == 200

    data = response.json()
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Jim","Incorrect first name"


