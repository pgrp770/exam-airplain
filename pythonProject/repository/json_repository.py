import json
from pythonProject.models import pilot as p
from pythonProject.models import aircraft as a


def write_cities_location(cities_location):
    with open('data/city_location.json', 'w') as f:
        json.dump(cities_location, f, indent=4)


def read_cities_location():
    with open('data/city_location.json', 'r') as f:
        cities_location = json.load(f)
        return cities_location


def read_cities_weather():
    with open('data/city_weather.json', 'r') as f:
        cities_weather = json.load(f)
        return cities_weather


def read_pilots_from_json():
    with open('data/pilots.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    return [p.Pilot(pilot['name'], pilot['skill']) for pilot in data["pilots"]]


def read_aircraft_from_json():
    with open('data/aircrafts.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    return [a.AirCraft(aircraft["type"], aircraft["speed"], aircraft["fuel_capacity"]) for aircraft in data["aircraft"]]


def write_cities_weather(cities_whether):
    with open('data/city_weather.json', 'w') as f:
        json.dump(cities_whether, f, indent=4)

#
# class PersonEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, AirCraft):
#             return obj.__dict__
#         return super().default(obj)
#
#
# def write_objects_to_json(objects, filename: str):
#     with open(filename, 'w') as jsonfile:
#         json.dump(objects, jsonfile, cls=PersonEncoder, indent=4)
#
#
# def read_people_from_json(filename: str):
#     with open(filename, 'r') as jsonfile:
#         data = json.load(jsonfile)
#     return [Person(person['name'], person['age']) for person in data]
#
#
# def write_person_to_json(person: Person, filename: str):
#     with open(filename, 'w') as jsonfile:
#         json.dump(person.__dict__, jsonfile, indent=4)
#
#
# def read_person_from_json(filename: str) -> Person:
#     with open(filename, 'r') as jsonfile:
#         data = json.load(jsonfile)
#     return Person(data['name'], data['age'])