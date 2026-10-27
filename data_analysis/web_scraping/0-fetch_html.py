#!/usr/bin/env python3
"""Download the raw HTML of a web page."""
import requests


def fetch_html(url, headers=None, timeout=10):
    """Return the body of `url` as text.

    headers: optional dict of HTTP headers (e.g. a User-Agent)
    timeout: seconds to wait for the server before giving up
    """
    response = requests.get(url=url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text
