#!/usr/bin/env python3
"""Print a GitHub user's location."""

import sys
import requests
from datetime import datetime, timezone


def main():
    """Fetch and print the user's location."""
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code == 200:
        user = response.json()
        print(user.get("location"))

    elif response.status_code == 404:
        print("Not found")

    elif response.status_code == 403:
        reset_timestamp = int(response.headers["X-Ratelimit-Reset"])
        now_timestamp = datetime.now(timezone.utc).timestamp()

        minutes = int((reset_timestamp - now_timestamp) / 60)
        print(f"Reset in {minutes} min")


if __name__ == "__main__":
    main()
