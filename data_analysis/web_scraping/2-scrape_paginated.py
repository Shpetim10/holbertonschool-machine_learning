#!/usr/bin/env python3
"""Scrape the quotes of every page of Quotes to Scrape."""
from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Return the quotes of all pages, starting at `base_url`.

    Follows the "Next" link of each page until there is none, or until a
    page that was already visited is reached. Waits one second between
    pages to avoid hammering the server.
    """
    url = base_url
    all_quotes = []
    cache = {}

    while url:
        # scrape the quotes of this page
        quotes = scrape_basic(url)
        all_quotes.extend(quotes)

        # fetch the page again to look for the "Next" link
        page = fetch_html(url)
        soup = BeautifulSoup(page, "html.parser")

        # remember the page so it is not visited twice
        cache[url] = page

        # build the absolute URL of the next page (None on the last one)
        next_link = soup.select_one("li.next a")
        url = parse.urljoin(url, next_link["href"]) if next_link else None

        # stop if the next page was already visited (avoids loops)
        if url in cache:
            break

        time.sleep(1)

    return all_quotes
