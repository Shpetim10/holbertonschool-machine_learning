# APIs

Introductory exercises on consuming a REST API from Python 3 with the
`requests` module. The data comes from the Star Wars API (SWAPI) mirror
hosted by Holberton: `https://swapi-api.hbtn.io/api/`.

## Quick start

```bash
pip install requests
cd pipeline/apis
./0-main.py            # every N-main.py runs the matching task
```

Each exercise is a pair: `N-name.py` holds the solution and `N-main.py` is a
small script that imports it (with `__import__`, because the file names start
with a digit) and prints the result. The scripts need an internet connection.

## Progress

| Task | File | Status |
| --- | --- | --- |
| 0 | `0-passengers.py` | Done |
| 1 | `1-sentience.py` | Not started (only the shebang line) |
| 2 | `2-user_location.py` | Not started (empty file) |

1 of 3 tasks implemented so far.

## Files

| File | Description |
| --- | --- |
| `0-passengers.py` | `availableShips(passengerCount)`: returns the names of the starships that can hold at least `passengerCount` passengers |
| `0-main.py` | Test script for task 0: prints the ships that hold 4 or more passengers |
| `1-sentience.py` | Placeholder for `sentientPlanets()`: planets that are home to sentient species |
| `1-main.py` | Test script for task 1: prints every planet returned by `sentientPlanets()` |
| `2-user_location.py` | Empty placeholder for the GitHub user location task |

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

## Requirements and style

- Python 3 with the `requests` module
- Files start with `#!/usr/bin/env python3` and are executable
- Code follows `pycodestyle`; every module and function has a docstring
