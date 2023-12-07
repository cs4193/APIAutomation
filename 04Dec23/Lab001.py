import requests


def main():
    # GET URL
    resonse_body = requests.get("https://restful-booker.herokuapp.com/booking/1")
    print(resonse_body.text)
    print(resonse_body.status_code)
    print(resonse_body.json())
    if resonse_body.status_code == 200:
        print("TC#001 - GET request is successful")
    else:
        print("TC#001 - GET request is not successful")


if __name__ == "__main__":
    main()

