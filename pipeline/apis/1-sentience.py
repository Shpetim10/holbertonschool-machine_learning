#!/usr/bin/env python3
"""Return the home planets of all sentient species."""

import requests


def sentientPlanets():
    """Return a list of unique sentient species' home planets."""
    url = "https://swapi-api.hbtn.io/api/species"
    homeworlds_cache = {}

    while url:
        response = requests.get(url)
        response.raise_for_status()
        species_data = response.json()

        for specie in species_data.get("results", []):
            if (
                specie.get("classification") == "sentient"
                or specie.get("designation") == "sentient"
            ):
                homeworld_url = specie.get("homeworld")

                if homeworld_url and homeworld_url not in homeworlds_cache:
                    planet_response = requests.get(homeworld_url)
                    planet_response.raise_for_status()
                    planet = planet_response.json()

                    planet_name = planet.get("name")
                    planet_id = int(
                        homeworld_url.rstrip("/").split("/")[-1]
                    )

                    homeworlds_cache[homeworld_url] = (
                        planet_id,
                        planet_name,
                    )

        url = species_data.get("next")

    return [
        name for planet_id, name in sorted(homeworlds_cache.values())
    ]
