import sys
import requests

def main():
    api_key = "b461e225dcc7bee4019c267ad50b7109"
    city = input("City: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)

    if response.status_code == 200:
        weather_info = response.json()
    else:
        print(f"Could not retrieve data {response.status_code}")

    try:
        if weather_info:
            print(f"the temperature in {weather_info["name"]} is {weather_info["main"]["temp"]}°F.")
    except:
        print("There was an error")

if __name__ == "__main__":
    main()