#!/usr/bin/env python3
"""Scrape the products of a static e-commerce category page."""

from selenium import webdriver


def scrape_products(url):
    """Return the products listed on the page at `url`.

    The page is rendered by headless Chrome through Selenium. Each product
    is a dict with the keys "title", "price", "description" and "rating"
    (the number of stars, as an int). The browser is always closed.
    """
    # run Chrome without a window, with a fixed size so the layout is stable
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        # every product sits in its own "thumbnail" card
        cards = driver.find_elements(
            "css selector", "div.thumbnail"
        )

        products = []

        for card in cards:
            # the full title is in the link's title attribute, because the
            # visible link text is cut short
            title = card.find_element(
                "css selector", "a.title"
            ).get_attribute("title")

            price = card.find_element(
                "css selector", "h4.price"
            ).text

            description = card.find_element(
                "css selector", "p.description"
            ).text

            # the number of stars is stored in the data-rating attribute
            rating = int(card.find_element(
                "css selector", ".ratings p[data-rating]"
            ).get_attribute("data-rating"))

            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": rating
            })

        return products

    finally:
        driver.quit()


def scrape_products_list(url):
    """Return the products at `url`; the name used by 6-main.py."""
    return scrape_products(url)
