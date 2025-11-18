# NeighborAPI
API for Neighbor's take home project

To use the API, make curl requests of the format

```bash
curl -X POST "https://API_URL/" \
        -H "Content-Type: application/json" \
        -d ' 
        [
          {
            "length": 10,
            "quantity": 1
          },
          {
            "length": 20,
            "quantity": 2
          }
        ]
```

the returned payload will be in the following json format

```json
[
  {
    "location_id": "abc123",
    "listing_ids": ["def456", "ghi789", "jkl012"],
    "total_price_in_cents": 300
  },
  {
    "location_id": "mno345",
    "listing_ids": ["pqr678", "stu901"],
    "total_price_in_cents": 305
  }
]
```
this list of json objects will contain:

every possible location that could store all requested vehicles

the cheapest possible combination of listings per location

only one result per location_id

and be sorted by the total price in cents, ascending

