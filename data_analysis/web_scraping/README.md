# Web Scraping

Introductory exercises on collecting data from the web with Python 3, using the
`requests` and `beautifulsoup4` modules. Every task scrapes quotes from
[Quotes to Scrape](https://quotes.toscrape.com/), a site built for practising
scraping, and returns them as a list of dicts:

```python
{"text": "...", "author": "...", "tags": ["...", "..."]}
```

## Quick start

```bash
pip install requests beautifulsoup4
cd data_analysis/web_scraping
./1-main.py            # every N-main.py runs the matching task
```

Each exercise is a pair: `N-name.py` holds the solution and `N-main.py` is a
small script that imports it (with `__import__`, because the file names start
with a digit) and prints the result. The scripts need an internet connection.

## Progress

| Task | File | Status |
| --- | --- | --- |
| 0 | `0-fetch_html.py` | Done |
| 1 | `1-scrape_basic.py` | Done |
| 2 | `2-scrape_paginated.py` | Done |
| 3 | `3-scrape_via_api.py` | Done |
| 4 | `4-extract_jsonld.py` | Done |
| 5 | `5-login_and_scrape.py` | Done |
| 6 | `6-products_list.py` | Not started |
| 7 | `7-product_detail.py` | Not started |
| 8 | `8-scroll_and_scrape.py` | Not started |

6 of 9 tasks implemented (tasks 0–5).

## Files

| File | Description |
| --- | --- |
| `0-fetch_html.py` | `fetch_html(url, headers=None, timeout=10)`: returns the HTML of a page as text |
| `0-main.py` | Test script for task 0: fetches a valid page, a non-existent site, and compares responses with and without a browser `User-Agent` |
| `1-scrape_basic.py` | `scrape_basic(url)`: returns the quotes of one page |
| `1-main.py` | Test script for task 1: prints the first two quotes of the home page |
| `2-scrape_paginated.py` | `scrape_paginated(base_url)`: returns the quotes of every page |
| `2-main.py` | Test script for task 2: prints the first quote found |
| `3-scrape_via_api.py` | `scrape_via_api(base_url)`: returns the quotes read from the JSON API |
| `3-main.py` | Test script for task 3: prints every quote |
| `4-extract_jsonld.py` | `extract_jsonld(url)`: returns the quotes described by the JSON-LD blocks of a page |
| `4-main.py` | Test script for task 4: replaces `fetch_html` with a fake page, so no network is needed |
| `5-login_and_scrape.py` | `login_and_scrape(login_url, user, pwd)`: logs in, then returns the quotes |
| `5-main.py` | Test script for task 5: logs in with a test account and prints every quote |

## How each task works

### Task 0: fetch a page

`fetch_html` sends a `GET` request with `requests.get` and returns the
response body (`response.text`). Optional `headers` let the caller send a
`User-Agent`, since some sites answer differently to scripts than to browsers,
and `timeout` stops the call from hanging forever.

### Task 1: parse one page

The HTML from task 0 is parsed with BeautifulSoup and CSS selectors:

| Field | Selector |
| --- | --- |
| each quote | `div.quote` |
| text | `span.text` |
| author | `small.author` |
| tags | `a.tag` (one per tag) |

### Task 2: follow the pages

```
 page 1 ──► li.next a ──► page 2 ──► ... ──► no "Next" link
```

`scrape_paginated` scrapes a page with task 1, finds the `li.next a` link,
turns its relative `href` into an absolute URL with `urllib.parse.urljoin` and
repeats. It stops when there is no "Next" link, or when the next URL was
already visited (a cache of visited pages protects against loops). It sleeps
one second between pages to be polite to the server.

### Task 3: use the JSON API

Instead of parsing HTML, the site's own endpoint `/api/quotes?page=N` is
called. Each response looks like this:

```
{"quotes": [{"text": ..., "author": {"name": ...}, "tags": [...]}, ...],
 "has_next": true}
```

Pages are requested one after another while `has_next` is true. The author's
name is taken from the nested `author` object so the result has the same shape
as in the other tasks.

### Task 4: read JSON-LD

Some pages embed structured data in
`<script type="application/ld+json">` tags. `extract_jsonld` finds those tags,
loads each one with `json.loads`, and maps `text`, `author.name` and
`keywords` to the common `text`, `author` and `tags` keys. The main file
swaps `fetch_html` for a fake function that returns a small page, so the task
can be tested without a network.

### Task 5: log in

```
 GET /login ──► read csrf_token ──► POST /login ──► GET / (as logged-in user)
```

A `requests.Session` keeps the cookies from one request to the next. The login
form contains a hidden `csrf_token` field, so the login page is fetched first
and the token is sent back with the username and password. After the login the
home page is requested with the same session and parsed like in task 1.

## Requirements and style

- Python 3 with `requests` and `beautifulsoup4`
- Files start with `#!/usr/bin/env python3` and are executable
- Code follows `pycodestyle`; every module and function has a docstring
