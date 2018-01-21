import sys
import json
from os.path import exists


def load_data(filepath):
    with open(filepath) as json_file:
        return json_file.read()


def get_biggest_bar(bars):
    return max(bars, key=lambda bar:
        bar["properties"]["Attributes"]["SeatsCount"]
    )


def get_smallest_bar(bars):
    return min(bars, key=lambda bar:
        bar["properties"]["Attributes"]["SeatsCount"]
    )


def get_closest_bar(bars, longitude, latitude):
    sum_coordinats = float(longitude) + float(latitude)
    return min(bars, key=lambda bar:
            abs(
                sum(bar["geometry"]["coordinates"]) - sum_coordinats
            )
    )


def print_info_bar(operation, bar):
    print(
        "{0} name bar = {1}, SeatsCount = {2}".format(
            operation,
            bar["properties"]["Attributes"]["Name"],
            bar["properties"]["Attributes"]["SeatsCount"]
        )
    )


def input_coordinates(user_number):
    coordinates = input(user_number)
    try:
        return float(coordinates)
    except ValueError:
        return None


if __name__ == '__main__':
    if len(sys.argv) != 2 or not exists(sys.argv[1]):
        sys.exit("The file doesn't exist!")
    file_path = sys.argv[1]
    bars = json.loads(load_data(file_path))["features"]
    biggest_bars = get_biggest_bar(bars)
    smallest_bars = get_smallest_bar(bars)
    print_info_bar("Max", biggest_bars)
    print_info_bar("Min", smallest_bars)
    longitude = input_coordinates("Input our longitude: >> ")
    latitude = input_coordinates("Input our latitude: >> ")
    if longitude and latitude:
        our_closest_bar = get_closest_bar(bars, longitude, latitude)
        print_info_bar("Closest", our_closest_bar)
    else:
        print("Bad coordinates")