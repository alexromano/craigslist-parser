# adapted from https://github.com/ryanirl/CraigslistScraper/
from urllib.parse import quote
import json
import csv
import os

from typing import List
from typing import Dict

# Get the directory of the current file agnositc of library location.
cs_dir = os.path.dirname(os.path.abspath(__file__))


# def get_us_cities() -> List[str]:
#     path = os.path.join(cs_dir, "data/us_cities.csv")
#     with open(path, "r") as file:
#         reader = csv.reader(file)
#         cities = [city[0] for city in reader]
#     return cities


def format_price(price: str) -> float:
    return float(price.replace("$", "").replace(",", ""))


def build_url(query: str, city: str, category: str = "sss") -> str:
    return f"https://{city}.craigslist.org/search/{category}?query={quote(query)}"


def get_neighborhood_values(names: List[str]) -> List[Dict]:
    with open(os.path.join(cs_dir, "data/neighborhoods.json"), "r") as file:
        neighborhoods = json.load(file)
    return list(map(lambda x: x["value"], filter(lambda n: n["name"] in names, neighborhoods)))

# def get_areas() -> List[Dict]:
#     with open(os.path.join(cs_dir, "data/areas.json"), "r") as file:
#         areas = json.load(file)
#     return areas


# def get_categories() -> List[Dict]:
#     with open(os.path.join(cs_dir, "data/categories.json"), "r") as file:
#         categories = json.load(file)
#     return categories


# laundry=1&laundry=2&laundry=3&max_price=3500&nh=10&nh=11&nh=12&nh=14&nh=149&nh=15&nh=2&nh=21&nh=4&nh=5&nh=9&query=month%20to%20month#search=1~list~0~10
