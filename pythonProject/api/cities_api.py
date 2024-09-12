import requests
import json

cities = [
    "Gaza Strip", "Damascus", "Beirut", "Amman", "Cairo", "Baghdad", "Tehran", "Riyadh",
    "Tripoli", "Ankara", "Khartoum", "Sanaa", "Manama",
    "Kuwait City", "Doha", "Jerusalem"
]
api_key = "6925c8df66b713a631d3be48827cdfba"


def get_cities_location():
    res = {}

    for city in cities:
        try:
            url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=2&appid={api_key}"
            response = requests.get(url)

            if response.status_code == 200:
                city_data = response.json()
                res[city] = city_data
            else:
                print(response.status_code)

        except Exception as e:
            print(e)
            return
    return res


def get_cities_weather():
    res = {}

    for city in cities:
        try:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
            response = requests.get(url)

            if response.status_code == 200:
                city_data = response.json()
                res[city] = city_data
            else:
                print(response.status_code)

        except Exception as e:
            print(e)
            return
    return res

