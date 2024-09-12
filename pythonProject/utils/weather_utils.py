from toolz import *


weather_score = {
    "Clear": 1.0,
    "Clouds": 0.7,
    "Rain": 0.4,
    "Stormy": 0.2
}


def get_city_name(d):
    return list(d.keys())[0]


def get_city_location(d, v):
    return list(d.values())[0][0][v]


def get_points_from_weather(weather):
    if weather in weather_score:
        return weather_score[weather]
    return 0


def get_cities_weather(cities_weather):
    return pipe(
        [[key, val] for key, val in cities_weather.items()],
        partial(map, lambda x: [x[0],  # city name
                                # get_points_from_weather(get_in([1, "list", 0, "weather", 0, "main"], x)),
                                get_in([1, "list", 0, "wind", "speed"], x),
                                get_in([1, "list", 0, "clouds", "all"], x),
                                get_in([1, "list", 0, "weather", 0, "main"], x),
                                # get_in([1, "list", 0, "wind", "speed"], x),  # speed of the wind
                                # get_in([1, "list", 0, "clouds", "all"], x),  # clouds in the city


                                ]),
        list
    )


def get_points_weather(wind, clouds, weather):
    '''
    weather_point = 20%
    clouds = 5%
    wind = 5%
    weather = 10%
    '''
    weather_points = get_points_from_weather(weather)*0.5


    max_wind = 12
    wind_point = (1-wind/max_wind)*0.25

    max_cloud = 100
    cloud_point = (1-clouds/max_cloud)*0.25

    return (weather_points + wind_point + cloud_point)*0.2








# def get_max_distance(cities_distance):
#     return pipe(
#         cities_distance,
#         partial(max, key=lambda x: list(x.values())[0]),
#         lambda x: list(x.values())[0]
#     )
#
# def get_points_distance():
#     pass
