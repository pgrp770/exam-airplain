from toolz import pipe, first
from toolz.curried import partial, partition

from api import cities_api
from pythonProject.models.aircraft import AirCraft
from pythonProject.models.pilot import Pilot
from pythonProject.utils.points_cities_utils import get_city_priority_distance_weather_list
from repository import json_repository as jr
from utils import distance_utils as du
from utils import weather_utils as wu
from utils import points_utils as pu
from utils import points_cities_utils

if __name__ == '__main__':

    # here you can get the cities location and cities whether

    # a = cities_api.get_cities_location()
    # json_repository.write_cities_location(a)
    # a = cities_api.get_cities_weather()
    # json_repository.write_cities_weather(a)
    #

    # tests distance

    cities_location = jr.read_cities_location()
    # print(cities_location)
    a = du.get_cities_distance(cities_location)
    # print(list(a))

    # print(du.get_max_distance(a))
    #
    # cities_weather = jr.read_cities_weather()
    # print(cities_weather)
    # b = list(wu.get_cities_weather(cities_weather))
    # print(list(b))
    #
    max_distance = du.get_max_distance(a)
    # print(pu.get_points_distance(a[10][1],max_distance[1]))
    # print(get_city_priority_distance_weather_list(a, b))
    # print(pu.get_pilot_point(Pilot("sdf", 7)))
    aircrafts = jr.read_aircraft_from_json()
    pilots = jr.read_pilots_from_json()
    weathers = wu.get_cities_weather(jr.read_cities_weather())
    distances = du.get_cities_distance(jr.read_cities_location())
    cities = get_city_priority_distance_weather_list(weathers, distances)
    print(weathers)
    print(distances)
    print(cities)

    mission_list = [
                    [weather[0],  # city name
                     points_cities_utils.cities_priority[weather[0]],  # priority
                     pilot,
                     air,
                     weather[1:],
                     distance[1:]

                     ]
                    for air in aircrafts for pilot in pilots for weather in weathers for distance in distances ]

    mission_list = []
    for air in aircrafts:
        for pilot in pilots:
            for weather, distance in zip(weathers , distances):
                    mission_list.append([weather[0],  # city name
                     points_cities_utils.cities_priority[weather[0]],  # priority
                     pilot,
                     air,
                     weather[1:],
                     distance[1:]
                     ])

    add_score = partial(map, lambda x: x + [
        pu.get_pilot_point(x[2]) +
                       pu.get_aircraft_point(x[3]) +
                       pu.get_prioraty_points(x[1]) +
                       pu.get_weather_points(x[-2][0], x[-2][1], wu.get_points_from_weather(x[-2][2])) +
                       pu.get_distance_points(x[-1][0], max_distance[1])
    ])
    list_by_pilots = pipe(
        mission_list,
        add_score,
        partial(map, lambda x: [x[0], x[1], x[2].name, x[3].aircraft_type, x[-2][0], x[-3][-1], x[2].skill, x[3].speed, x[3].fuel_capacity, x[-1]]),
        partial(filter, lambda x: x[0] != 'Jerusalem'),
        partial(sorted, key=lambda x:x[2]),
        partial(partition, 105, pad=None),
        partial(map, partial(sorted, key=lambda x:x[-1])),
        partial(map, lambda x: x[::-1]),
        list,

    )
    print(list_by_pilots)
    # p1, p2, p3, p4, p5, p6, p7, p8 = list_by_pilots[0], list_by_pilots[1], list_by_pilots[2],list_by_pilots[3],list_by_pilots[4],list_by_pilots[5],list_by_pilots[6], list_by_pilots[7]
    # print(p2)
    def remove_air_target(li, target, air):
        return pipe(
            li,
            partial(filter, lambda x: x[0]!=target),
            partial(filter, lambda x: x[3]!=air),
            list,

        )
    first_mission = first(list_by_pilots[0])
    a = [first_mission]

    # for v in a:
    #     list_by_pilots[1] = remove_air_target(list_by_pilots[1], v[0], v[3])
    # print(first(list_by_pilots[1]))
    # a+= list_by_pilots[1]
    # for v in a:
    #     list_by_pilots[2] = remove_air_target(list_by_pilots[2], v[0], v[3])
    # print(first(list_by_pilots[2]))
    # second_mission = remove_air_target(first_mission, first_mission[0], first_mission[3])
    # print(second_mission)
    # three_mission = remove_air_target(second_mission, second_mission[0], second_mission[3])
    # print(three_mission)
    #
    # missino4 = remove_air_target(three_mission, three_mission[0], three_mission[3])
    # print(missino4)
    # mission5 = remove_air_target(missino4, missino4[0], missino4[3])
    # print(missino5)
    # mission6 = remove_air_target(mission5, mission5[0], mission5[3])
    # mission7 = remove_air_target(mission6, mission6[0], mission6[3])
    # mission8 = remove_air_target(mission7, mission7[0], mission7[3])
    #
    #
