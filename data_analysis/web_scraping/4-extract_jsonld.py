#!/usr/bin/env python3
"""Extract quote data from the JSON-LD blocks embedded in a page."""
import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Return the quotes described by the JSON-LD scripts at `url`.

    Reads every <script type="application/ld+json"> tag and maps it to a
    dict with the keys "text", "author" (the author's name) and "tags"
    (taken from "keywords").
    """
    soup = BeautifulSoup(fetch_html(url), "html.parser")

    blocks = []

    for script in soup.select('script[type="application/ld+json"]'):
        obj = json.loads(script.string)
        blocks.append({
            "text": obj.get("text"),
            "author": obj.get("author").get("name"),
            "tags": obj.get("keywords")
        })

    return blocks
