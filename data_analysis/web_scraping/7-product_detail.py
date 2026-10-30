#!/usr/bin/env python3
"""Scrape the details of a single product page."""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_product_detail(url, delay=2.0):
    """Return the details of the product page at `url`.

    The result is a dict with the keys "title", "price", "description" and
    "rating" (the number of stars, as an int). `delay` is the number of
    seconds to wait after loading, so the page can finish rendering.
    """
    # run Chrome without a window, with a fixed size so the layout is stable
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        # give the page time to render before reading it
        time.sleep(delay)

        # the rating is the count of star icons, so find_elements is used
        return {
                "title": driver.find_element(
                    By.CSS_SELECTOR, ".caption h4.title"
                    ).text,
                "price": driver.find_element(
                    By.CSS_SELECTOR, ".caption h4.price"
                    ).text,
                "description": driver.find_element(
                    By.CSS_SELECTOR, ".caption p.description"
                    ).text,
                "rating": len(
                    driver.find_elements(
                        By.CSS_SELECTOR, ".ratings .ws-icon-star"
                        )
                    ),
            }

    finally:
        driver.quit()
