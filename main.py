from .lib import search as cs
from .lib.types import Categories, Neighborhoods, Laundry
import json

# Define the search. Everything is done lazily, and so the html is not 
# fetched at this step.

search = cs.Search(
    query = "",
    category = Categories.APARTMENT,
    city = "sfbay",
)

filters = {
    "max_bedrooms": 1,
    "max_price": 3500,
    "neighborhoods": [
        Neighborhoods.SOMA,
        Neighborhoods.USF
    ],
    "laundry": [Laundry.IN_UNIT, Laundry.ON_SITE, Laundry.IN_BUILDING],
}

# Fetch the html from the server. Don't forget to check the status. 
status = search.fetch(filters)
if status != 200:
    raise Exception(f"Unable to fetch search with status <{status}>.")

for ad in search.ads:
    # Fetch additional information about each ad. Check the status again.
    status = ad.fetch()
    if status != 200:
        print(f"Unable to fetch ad '{ad.title}' with status <{status}>.")
        continue

    # There is a to_dict() method for convenience. 
    data = ad.to_dict()

    # json.dumps is merely for pretty printing. 
    print(json.dumps(data, indent = 4))
