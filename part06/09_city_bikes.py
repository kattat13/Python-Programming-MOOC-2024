import math


def read_file(filename):
    data = []
    f = open(filename)
    table = f.read().strip().split('\n')
    for line in table[1:]:
        data.append(line.split(';'))
    return data


def get_station_data(filename: str):
    data = read_file(filename)
    station_dict = {}
    for x in data:
        station_dict[x[3]] = tuple((float(x[0]), float(x[1])))
    return station_dict


def distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


def greatest_distance(stations: dict):
    greatest = 0.0
    names = None
    for i in stations:
        for j in stations:
            dist = distance(stations, i, j)
            if dist > greatest:
                greatest = dist
                names = (i, j)
                
    return names[0], names[1], greatest
    

if __name__ == "__main__":
    stations = get_station_data('stations2.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)



    # stations = get_station_data('stations2.csv')
    # station1, station2, greatest = greatest_distance(stations)
    # print(station1, station2, greatest)
    