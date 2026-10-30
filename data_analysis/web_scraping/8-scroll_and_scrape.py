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

        # remember how many products are on the page before scrolling
        last_count = len(driver.find_elements(
            "css selector", "div.thumbnail"
        ))

        # scroll to the bottom until no more products are loaded
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            # wait for new products, but stop waiting as soon as they appear
            deadline = time.time() + scroll_pause
            new_count = last_count

            while new_count == last_count and time.time() < deadline:
                time.sleep(0.05)
                new_count = len(driver.find_elements(
                    "css selector", "div.thumbnail"
                ))

            # nothing new within `scroll_pause`, so every product is loaded
            if new_count == last_count:
                break

            last_count = new_count

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
                ".ratings span.ws-icon-star"
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
