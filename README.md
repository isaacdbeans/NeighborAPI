# NeighborAPI
API for Neighbor's take-home project

Look at example.py to see an example of making a request with the Python requests library

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

The returned payload will be in the following JSON format

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
This list of JSON objects will contain:

Every possible location that could store all the requested vehicles

The cheapest possible combination of listings per location

Only one result per location_id

The list will also be sorted by the total price in cents, ascending

