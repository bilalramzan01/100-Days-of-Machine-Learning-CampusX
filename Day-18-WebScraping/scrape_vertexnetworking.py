#!/usr/bin/env python3
"""
Scraper for vertexnetworking.co.uk
Walks every category -> subcategory -> product listing (with pagination),
visits each product page, and writes category / image / title / description
to a CSV file.

Requirements:
    pip install requests beautifulsoup4

Usage:
    python scrape_vertexnetworking.py

Output:
    vertexnetworking_products.csv
"""

import csv
import time
import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.vertexnetworking.co.uk"
OUTPUT_CSV = "vertexnetworking_products.csv"
REQUEST_DELAY = 0.75   # seconds between requests, be polite to their server
TIMEOUT = 20

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

session = requests.Session()
session.headers.update(HEADERS)


def get_soup(url):
    """Fetch a URL and return a BeautifulSoup object, or None on failure."""
    try:
        resp = session.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        time.sleep(REQUEST_DELAY)
        return BeautifulSoup(resp.text, "html.parser")
    except requests.RequestException as e:
        print(f"  [warn] failed to fetch {url}: {e}")
        return None


def discover_category_links():
    """Find every /category/N and /subcategory/N link from the homepage nav."""
    soup = get_soup(BASE_URL)
    if soup is None:
        raise SystemExit("Could not load homepage — aborting.")

    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        full = urljoin(BASE_URL, href)
        if re.search(r"/(category|subcategory)/\d+", full):
            links.add(full)
    return sorted(links)


def get_category_label(soup, fallback_url):
    """Try to pull a readable category/subcategory name from a listing page."""
    # Try breadcrumb, h1, or <title>
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)
    title = soup.find("title")
    if title and title.get_text(strip=True):
        return title.get_text(strip=True).split("|")[0].strip()
    return fallback_url


def find_product_links(soup):
    """Extract all product detail page links from a listing page."""
    links = set()
    for a in soup.find_all("a", href=True):
        href = urljoin(BASE_URL, a["href"])
        if "/product/" in href and href.endswith(".html"):
            links.add(href)
    return links


def find_next_page(soup, current_url):
    """Look for a 'next page' pagination link."""
    # Common patterns: rel="next", a text "Next", or ?page=N links
    next_link = soup.find("a", rel="next")
    if next_link and next_link.get("href"):
        return urljoin(current_url, next_link["href"])

    for a in soup.find_all("a", href=True):
        text = a.get_text(strip=True).lower()
        if text in ("next", "»", "next »", ">"):
            return urljoin(current_url, a["href"])

    return None


def scrape_product(url, category_label):
    """Visit a product page and extract title, image, description."""
    soup = get_soup(url)
    if soup is None:
        return None

    # Title: prefer og:title, fall back to <h1>
    title = None
    og_title = soup.find("meta", property="og:title")
    if og_title and og_title.get("content"):
        title = og_title["content"].strip()
    if not title:
        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)

    # Image: prefer og:image, fall back to first product image
    image = None
    og_image = soup.find("meta", property="og:image")
    if og_image and og_image.get("content"):
        image = urljoin(url, og_image["content"].strip())
    if not image:
        img = soup.find("img", src=re.compile(r"/product_images/"))
        if img and img.get("src"):
            image = urljoin(url, img["src"])

    # Description: prefer meta description, fall back to a product
    # description container, fall back to og:description
    description = None
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        description = meta_desc["content"].strip()
    if not description:
        og_desc = soup.find("meta", property="og:description")
        if og_desc and og_desc.get("content"):
            description = og_desc["content"].strip()
    if not description:
        desc_div = soup.find(
            ["div", "section"],
            class_=re.compile(r"(description|product-desc|details)", re.I),
        )
        if desc_div:
            description = desc_div.get_text(" ", strip=True)

    return {
        "category": category_label,
        "image": image or "",
        "title": title or "",
        "description": description or "",
        "url": url,
    }


def main():
    print("Discovering category/subcategory links...")
    category_links = discover_category_links()
    print(f"Found {len(category_links)} category/subcategory links.")

    seen_products = {}  # url -> row dict, dedupe across categories

    for cat_url in category_links:
        print(f"\nCategory page: {cat_url}")
        page_url = cat_url
        visited_pages = set()

        while page_url and page_url not in visited_pages:
            visited_pages.add(page_url)
            soup = get_soup(page_url)
            if soup is None:
                break

            label = get_category_label(soup, cat_url)
            product_links = find_product_links(soup)
            print(f"  {page_url} -> {len(product_links)} product links")

            for p_url in product_links:
                if p_url in seen_products:
                    continue
                print(f"    scraping product: {p_url}")
                row = scrape_product(p_url, label)
                if row:
                    seen_products[p_url] = row

            page_url = find_next_page(soup, page_url)

    print(f"\nTotal unique products scraped: {len(seen_products)}")

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["category", "image", "title", "description", "url"]
        )
        writer.writeheader()
        for row in seen_products.values():
            writer.writerow(row)

    print(f"Saved to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
