#!/usr/bin/env python3
"""Log in to Quotes to Scrape and scrape the quotes as a user."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in at `login_url` with `user` and `pwd`, then return the quotes.

    A Session keeps the cookies between requests. The login form needs a
    CSRF token, so the login page is fetched first to read it. Each quote is
    a dict with the keys "text", "author" and "tags".
    """
    session = requests.Session()

    # load the login page and read the hidden CSRF token
    response = session.get(login_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    csrf_input = soup.find("input", {"name": "csrf_token"})
    csrf_token = csrf_input["value"]

    # submit the login form with the credentials and the token
    credentials = {
        "username": user,
        "password": pwd,
        "csrf_token": csrf_token,
    }

    response = session.post(login_url, data=credentials)
    response.raise_for_status()

    # request the home page, now as a logged-in user
    quotes_url = "https://quotes.toscrape.com/"
    response = session.get(quotes_url)
    response.raise_for_status()

    # extract the text, author and tags of every quote
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []

    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()

        tags = [
            tag.get_text()
            for tag in quote.find_all("a", class_="tag")
        ]

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags,
        })

    return quotes
