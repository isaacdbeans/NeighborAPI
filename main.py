import json
from fastapi import FastAPI
from pydantic import BaseModel
from itertools import combinations
from typing import List, Dict

app = FastAPI()

class Item(BaseModel):
    length: int
    quantity: int

def find_storage_options(vehicles: List[Dict], listings: List[Dict]):
    from collections import defaultdict

    # group listings by location
    listings_by_location = defaultdict(list)
    for listing in listings:
        listings_by_location[listing["location_id"]].append(listing)

    results = []

    # total vehicle lengths to store
    vehicle_units = []
    for v in vehicles:
        vehicle_units.extend([v["length"]] * v["quantity"])

    for location_id, loc_listings in listings_by_location.items():
        min_price = float("inf")
        best_combo = None

        # try all listing combinations (1 to len(loc_listings))
        for r in range(1, len(loc_listings) + 1):
            for combo in combinations(loc_listings, r):
                available_lengths = [l["length"] for l in combo]

                # simple greedy check if combo can store all vehicle units
                temp_units = sorted(vehicle_units, reverse=True)
                temp_lengths = sorted(available_lengths, reverse=True)

                fits = True
                for i, unit_len in enumerate(temp_units):
                    if i >= len(temp_lengths) or temp_lengths[i] < unit_len:
                        fits = False
                        break

                if fits:
                    total_price = sum(l["price_in_cents"] for l in combo)
                    if total_price < min_price:
                        min_price = total_price
                        best_combo = combo

        if best_combo:
            results.append({
                "location_id": location_id,
                "listing_ids": [l["id"] for l in best_combo],
                "total_price_in_cents": min_price
            })

    # sort by total price ascending
    return sorted(results, key=lambda x: x["total_price_in_cents"])

@app.post("/")
async def process_items(items: List[Item]):
    vehicles = [{"length": item.length, "quantity": item.quantity} for item in items]

    with open("listings.json", "r") as f:
        listings = json.load(f)

    results = find_storage_options(vehicles, listings)
    return results
