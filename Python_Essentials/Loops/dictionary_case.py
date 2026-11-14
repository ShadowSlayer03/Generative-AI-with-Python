users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "P50"},
    {"id": 3, "total": 50, "coupon": "P80"},
    {"id": 4, "total": 260, "coupon": "P10"},
]

discounts = {
    "P20": (0.2,0),
    "P50": (0.5,0),
    "P80": (0.8,0),
    "P10": (0.1,10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"])
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} got total bill of Rs {user["total"]} but got discount of Rs {discount}")