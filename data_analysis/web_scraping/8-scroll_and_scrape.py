#!/usr/bin/env python3
"""Scrape the products of an infinite-scroll page."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll to the bottom of the page at `url` and return its products.

    More products are loaded each time the page is scrolled down, so the
    scrolling repeats until the page stops growing. Each product is a dict
    with the keys "title", "price", "description" and "rating" (the number
    of stars, as an int). Products seen twice are returned only once.
    `scroll_pause` is the number of seconds to wait after each scroll.
    """
    # run Chrome without a window, with a fixed size so the layout is stable
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        # remember the height of the page before scrolling
        last_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        # scroll to the bottom until the page height stops increasing
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            # wait for the new products to load
            time.sleep(scroll_pause)

            new_height = driver.execute_script(
                "return document.body.scrollHeight"
            )

            # no new content was loaded, so every product is on the page
            if new_height == last_height:
                break

            last_height = new_height

        # read every product card now that the page is fully loaded
        cards = driver.find_elements(
            "css selector", "div.thumbnail"
        )

        products = []
        seen = set()

        for card in cards:
            title = card.find_element(
                "css selector", "a.title"
            ).get_attribute("title")

            price = card.find_element(
                "css selector", "h4.price"
            ).text

            description = card.find_element(
                "css selector", "p.description"
            ).text

            rating = len(card.find_elements(
                "css selector",
                ".ratings p.ws-icon.ws-icon-star"
            ))

            # skip a product that was already added (same title and price)
            key = (title, price)

            if key not in seen:
                seen.add(key)

                products.append({
                    "title": title,
                    "price": price,
                    "description": description,
                    "rating": rating
                })

        return products

    finally:
        driver.quit()
