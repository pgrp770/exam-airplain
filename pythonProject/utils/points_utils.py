def get_distance_points(city_distance, max_city):
    '''
    distance = 20%
    '''
    return (1 - city_distance/max_city)*0.2


def get_weather_points(wind, clouds, weather_point):
    '''
    weather_point = 20%
    clouds = 5%
    wind = 5%
    weather = 10%
    '''
    weather_points = weather_point*0.5

    max_wind = 12
    wind_point = (1-wind/max_wind)*0.25

    max_cloud = 100
    cloud_point = (1-clouds/max_cloud)*0.25

    return (weather_points + wind_point + cloud_point)*0.2


def get_pilot_point(pilot):
    '''
    pilot point = 25%
    the max skill is 10 and min skill is 5
    there for the range of the skill is five points
    and every point is 20%
    '''

    return (pilot.skill - 5)/5*0.25


def get_aircraft_point(aircraft):
    '''
    aircraft = 25%
    speed = 30% from aircraft
    fuel_capacity = 70% from aircraft
    max speed = 1800
    fuel_capacity = 6000
    '''
    return (aircraft.speed/1800*0.3 + aircraft.fuel_capacity/6000*0.7)*0.25

def get_prioraty_points(prioraty):
    '''
    prioraty = 10%
    '''

    return (prioraty/5)*0.1

