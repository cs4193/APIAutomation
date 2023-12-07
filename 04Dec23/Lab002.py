import requests


def main():
    # GET URL
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/538")
    assert response_body.status_code == 200
    data = response_body.json()

    assert "firstname" in data, "First name field is not present "
    assert "lastname" in data, "Last name field is not present "

    #assert  data['firstname'] == "Josh", "Incorrect first name is Josh"

if __name__ == "__main__":
    main()

