#!/usr/bin/env python3
"""Scrape the quotes of Quotes to Scrape through its JSON API."""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Return the quotes served by `base_url`/api/quotes.

    The API is paginated: each response has a "has_next" flag that tells
    whether another page exists. Each quote is a dict with the keys "text",
    "author" (the author's name) and "tags".
    """
    quotes = []
    page = 1

    while True:
        payload = json.loads(fetch_html(f"{base_url}/api/quotes?page={page}"))
        for item in payload["quotes"]:
            quotes.append({
                "text": item["text"],
                "author": item["author"]["name"],
                "tags": item["tags"]
            })

        if not payload.get("has_next"):
            break

        page += 1

    return quotes
