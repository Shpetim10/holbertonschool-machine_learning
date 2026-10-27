#!/usr/bin/env python3
"""Scrape the quotes of a single page of Quotes to Scrape."""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Return the quotes found on the page at `url`.

    Each quote is a dict with the keys "text", "author" and "tags"
    (a list of tag names).
    """
    page = fetch_html(url)
    soup = BeautifulSoup(page, "html.parser")
    quotes = []

    for block in soup.select("div.quote"):
        quotes.append({
            "text": block.select_one("span.text").get_text(strip=True),
            "author": block.select_one("small.author").get_text(strip=True),
            "tags": [tag.get_text(strip=True) for tag in block.select("a.tag")]
        })

    return quotes
