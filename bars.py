import sys
import json
import numpy as np
from os.path import exists, isfile


def load_data(filepath):
    with open(filepath) as bars:
        return bars.read()


def get_biggest_bar(bars):
    max_seatscount = max([bar["seatscount"] for bar in bars])
    return [
        bar for bar in bars if bar["seatscount"] == max_seatscount
    ]


def get_smallest_bar(bars):
    min_seatscount = min([bar["seatscount"] for bar in bars])
    return [
        bar for bar in bars if bar["seatscount"] == min_seatscount
    ]


def get_closest_bar(bars, longitude, latitude):
    array = np.array(
        [
            bar["coordinates"] for bar in bars
        ]
    )
    idx = np.array(
        [
            np.linalg.norm(x+y)
            for (x, y) in array - [longitude, latitude]
        ]
    ).argmin()
    return bars[idx]


def print_max_bar(bars):
    for bar in bars:
        print(
            "Max name bar = {0}, SeatsCount = {1}".format(
                bar["name"],
                bar["seatscount"]
            )
        )


def print_min_bar(bars):
    for bar in bars:
        print(
            "Min name bar = {0}, SeatsCount = {1}".format(
                bar["name"],
                bar["seatscount"]
            )
        )


def print_closest_bar(bar):
    print(
        "Closets name bar = {0}".format(bar["name"])
    )


if __name__ == '__main__':
    file_path = sys.argv[1]
    if exists(file_path) and isfile(file_path):
        root = json.loads(load_data(file_path))["features"]
        get_attributes_bars = [
            {
                "coordinates": bar["geometry"]["coordinates"],
                "global_id": bar["properties"]["Attributes"]["global_id"],
                "name": bar["properties"]["Attributes"]["Name"],
                "seatscount": bar["properties"]["Attributes"]["SeatsCount"]
            }
            for bar in root
        ]
        max_seats_count = get_biggest_bar(get_attributes_bars)
        min_seats_count = get_smallest_bar(get_attributes_bars)
        print_max_bar(max_seats_count)
        print_min_bar(min_seats_count)
        longitude = np.float64(input("Input our longitude: >> "))
        latitude = np.float64(input("Input our latitude: >> "))
        our_closest_bar = get_closest_bar(
            get_attributes_bars, longitude, latitude
        )
        print_closest_bar(our_closest_bar)
    else:
        print("The file doesn't exist!")