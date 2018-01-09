import json
import numpy as np


def load_data(filepath):
    with open(filepath) as bars:
        return bars.read()


def get_biggest_bar(data):
    return max([bar["seatscount"] for bar in data])


def get_smallest_bar(data):
    return min([bar["seatscount"] for bar in data])


def get_closest_bar(data, longitude, latitude):
    array = np.array(
        [
            coordinates["coordinates"] for coordinates in data
        ]
    )
    idx = (np.abs(array - [longitude, latitude])).argmin(axis=0)
    for i, x in enumerate(np.abs(array - [longitude, latitude])):
        print(idx, i, x)
    return array[idx]


if __name__ == '__main__':
    root = json.loads(load_data("bars.json"))["features"]
    get_attributes_bars = [
        {
            "coordinates": bar["geometry"]["coordinates"],
            "global_id": bar["properties"]["Attributes"]["global_id"],
            "name": bar["properties"]["Attributes"]["Name"],
            "seatscount": bar["properties"]["Attributes"]["SeatsCount"]
        }
        for bar in root
    ]

    print(get_attributes_bars)

    max_seats_count = get_biggest_bar(get_attributes_bars)
    min_seats_count = get_smallest_bar(get_attributes_bars)
    max_bars_seatscount = [
        bar for bar in get_attributes_bars if bar == max_seats_count
    ]
    min_bars_seatscount = [
        bar for bar in get_attributes_bars if bar == min_seats_count
    ]
    longitude = np.float64(input("Input our longitude: >> "))
    latitude = np.float64(input("Input our latitude: >> "))
    our_closest_bar = get_closest_bar(
        get_attributes_bars, longitude, latitude
    )

    print(our_closest_bar)

#37.750290923482424, 55.61870614052117