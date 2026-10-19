#!/usr/bin/env python3
"""Return the starships that can hold a given number of passengers"""
import requests


def availableShips(passengerCount):
    """Return the names of the starships that hold at least passengerCount"""
    url = "https://swapi-api.hbtn.io/api/starships"
    result = []

    while url:
        from_api = requests.get(url)
        data = from_api.json()
        starships = data["results"]

        for starship in starships:
            passengers = starship["passengers"]
            # skip ships with no usable capacity
            if passengers is None or passengers in ["n/a", "unknown"]:
                continue
            # remove thousands separators, like "1,000"
            elif int(passengers.strip().replace(",", "")) >= passengerCount:
                result.append(starship["name"])

        # follow the next page, None on the last one
        url = data["next"]

    return result
