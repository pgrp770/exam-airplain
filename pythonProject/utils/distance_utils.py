from toolz import *
import math


def calculate_distance(lat1, lon1, lat2, lon2):
    # Function to calculate the distance between two coordinates using the Haversine formula

    r = 6371.0  # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon /
                                                                                     2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance


israel_location = {"Jerusalem": (31.79592425, 31.79592425)}
calculate_distance_from_israel = curry(
                                calculate_distance,
                                       israel_location["Jerusalem"][0],
                                       israel_location["Jerusalem"][1]
                                )


def get_city_name(d):
    return list(d.keys())[0]


def get_city_location(d, v):
    return list(d.values())[0][0][v]


def get_cities_distance(cities_location):

    return pipe(
        [{key: val} for key, val in cities_location.items()],
        partial(
            map,
            lambda x: {get_city_name(x): (get_city_location(x, "lat"), get_city_location(x, "lon"))}),
        partial(map,
                lambda x: [get_city_name(x), calculate_distance_from_israel(x[get_city_name(x)][0],x[get_city_name(x)][1])]),
        list
    )


def get_max_distance(cities_distance):
    return pipe(
        cities_distance,
        partial(max, key=lambda x: x[1]),
        lambda x: list(x)
    )





