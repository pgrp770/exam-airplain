cities_priority = {
    "Gaza Strip": 5,
    "Damascus": 5,
    "Beirut": 4,
    "Amman": 3,
    "Cairo": 3,
    "Baghdad": 5,
    "Tehran": 4,
    "Riyadh": 3,
    "Tripoli": 4,
    "Ankara": 4,
    "Khartoum": 3,
    "Sanaa": 2,
    "Manama": 2,
    "Kuwait City": 3,
    "Doha": 4,
    "Jerusalem": 0
}


def get_city_priority_distance_weather_list(weather_list, distance_list):
    print(weather_list, distance_list)
    return [[weather[0], [cities_priority[weather[0]], weather[1], distance[1], weather[2]]] for distance in distance_list for weather in weather_list]
