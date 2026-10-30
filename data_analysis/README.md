# Data Analysis

Holberton School data analysis projects in Python 3: collecting data from the
web so it can be cleaned and analysed later.

## Contents

| Project | Topic | Exercises |
| --- | --- | --- |
| [`web_scraping/`](web_scraping/) | Scraping with `requests` and `beautifulsoup4` (fetching HTML, CSS selectors, pagination, a JSON API, JSON-LD data, logging in with a session) and with `selenium` (headless Chrome, product pages, infinite scroll) | All 9 tasks done (0–8) |

## From the web to a dataset

Not all data comes in a file. When it lives on a website, a scraper collects it:

```
 ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
 │  Fetch   │ → │  Parse   │ → │  Follow  │ → │  Return  │
 │ requests │   │ BS4 / JSON│  │ next page│   │ list of  │
 │ .get()   │   │          │   │ or API   │   │ dicts    │
 └──────────┘   └──────────┘   └──────────┘   └──────────┘
```

Pages that build their content with JavaScript (such as infinite scroll) are
not in the HTML that `requests` downloads. For those, Selenium drives a real
headless browser, so the page can be scrolled before it is read.

The list of dicts returned by the scrapers can be loaded straight into a
`pandas` DataFrame (see [`pipeline/pandas/`](../pipeline/pandas/)).

## Requirements

```bash
pip install requests beautifulsoup4 selenium
```

Tasks 6–8 also need Google Chrome installed.
