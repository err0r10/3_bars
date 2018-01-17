import sys
import json
from os.path import exists


def load_data(filepath):
    with open(filepath) as bars:
        return bars.read()


def get_biggest_bar(bars):
    return [
        max(bars, key=lambda bar: bar["seatscount"])
    ]


def get_smallest_bar(bars):
    return [
        min(bars, key=lambda bar: bar["seatscount"])
    ]


def get_closest_bar(bars, longitude, latitude):
    sum_coordinats = float(longitude) + float(latitude)
    return [
        min(bars, key=lambda bar:
            abs(
                sum(bar["coordinates"]) - sum_coordinats
            )
        )
    ]


def print_info_bar(operation, bars):
    for bar in bars:
        print(
            "{0} name bar = {1}, SeatsCount = {2}".format(
                operation,
                bar["name"],
                bar["seatscount"]
            )
        )


if __name__ == '__main__':
    if len(sys.argv) != 2 or not exists(sys.argv[1]):
        print("The file doesn't exist!")
        sys.exit(0)
    file_path = sys.argv[1]
    data_json = json.loads(load_data(file_path))["features"]
    get_attributes_bars = [
        {
            "coordinates": bar["geometry"]["coordinates"],
            "global_id": bar["properties"]["Attributes"]["global_id"],
            "name": bar["properties"]["Attributes"]["Name"],
            "seatscount": bar["properties"]["Attributes"]["SeatsCount"]
        }
        for bar in data_json
    ]
    biggest_bars = get_biggest_bar(get_attributes_bars)
    smallest_bars = get_smallest_bar(get_attributes_bars)
    print_info_bar("Max", biggest_bars)
    print_info_bar("Min", smallest_bars)
    longitude = input("Input our longitude: >> ")
    latitude = input("Input our latitude: >> ")
    our_closest_bar = get_closest_bar(
        get_attributes_bars, longitude, latitude
    )
    print_info_bar("Closets", our_closest_bar)