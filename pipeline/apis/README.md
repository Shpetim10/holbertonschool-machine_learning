# APIs

Introductory exercises on consuming a REST API from Python 3 with the
`requests` module. Tasks 0 and 1 use the Star Wars API (SWAPI) mirror hosted
by Holberton (`https://swapi-api.hbtn.io/api/`); task 2 uses the GitHub API
(`https://api.github.com/`).

## Quick start

```bash
pip install requests
cd pipeline/apis
./0-main.py            # every N-main.py runs the matching task
./2-user_location.py https://api.github.com/users/holbertonschool
```

Each exercise is a pair: `N-name.py` holds the solution and `N-main.py` is a
small script that imports it (with `__import__`, because the file names start
with a digit) and prints the result. Task 2 is a standalone script instead: it
takes the API URL as its first argument. The scripts need an internet
connection.

## Progress

| Task | File | Status |
| --- | --- | --- |
| 0 | `0-passengers.py` | Done |
| 1 | `1-sentience.py` | Done |
| 2 | `2-user_location.py` | Done |

All 3 tasks implemented.

## Files

| File | Description |
| --- | --- |
| `0-passengers.py` | `availableShips(passengerCount)`: returns the names of the starships that can hold at least `passengerCount` passengers |
| `0-main.py` | Test script for task 0: prints the ships that hold 4 or more passengers |
| `1-sentience.py` | `sentientPlanets()`: returns the names of the home planets of all sentient species |
| `1-main.py` | Test script for task 1: prints every planet returned by `sentientPlanets()` |
| `2-user_location.py` | Script that prints the location of a GitHub user, given the user's API URL |

## How task 0 works

The `/starships` endpoint is paginated: each response holds one page of
results plus a `next` link to the following page. `availableShips` follows
that link until it is `None`, so every starship is checked.

```
 GET /starships ──► results (page 1) ──► next ──► results (page 2) ──► ... ──► next = None
```

For each ship the `passengers` field is a string, so it is cleaned first:

- `None`, `"n/a"` and `"unknown"` are skipped
- thousands separators are removed (`"1,000"` becomes `1000`)
- the ship is kept when the number is `>= passengerCount`

## How task 1 works

`sentientPlanets` walks every page of the `/species` endpoint the same way as
task 0, following `next` until it is `None`.

```
 GET /species ──► species is sentient? ──► GET homeworld URL ──► planet name
```

- a species counts as sentient when its `classification` **or** its
  `designation` is `"sentient"`
- species with no `homeworld` (`None`) are skipped
- each homeworld URL is fetched only once; the results are cached in a dict, so
  a planet shared by several species appears once
- the list is sorted by the planet id taken from the end of the URL
  (`.../planets/8/` → `8`), so the order matches the API's own order

## How task 2 works

`2-user_location.py` takes a full GitHub API user URL and reacts to the HTTP
status code of the response:

| Status | Meaning | Output |
| --- | --- | --- |
| `200` | User found | The `location` field (`None` if the user did not set one) |
| `404` | User does not exist | `Not found` |
| `403` | Rate limit exceeded | `Reset in X min`, where `X` is the number of minutes until the `X-Ratelimit-Reset` timestamp |

```bash
$ ./2-user_location.py https://api.github.com/users/holbertonschool
San Francisco, CA
$ ./2-user_location.py https://api.github.com/users/holberton_ho_no
Not found
$ ./2-user_location.py https://api.github.com/users/holbertonschool
Reset in 16 min
```

Unauthenticated requests to the GitHub API are limited to 60 per hour, which
is why the `403` case can show up after a few runs.

## Requirements and style

- Python 3 with the `requests` module
- Files start with `#!/usr/bin/env python3` and are executable
- Code follows `pycodestyle`; every module and function has a docstring
