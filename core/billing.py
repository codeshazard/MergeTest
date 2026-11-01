from typing import Union

TIER_DISCOUNTS = {
    "gold": 20.0,
    "silver": 10.0,
    "bronze": 5.0,
}

def calculate_discount(price: float, discount: Union[float, str]) -> float:
    """Calculate discount amount from an explicit percentage (e.g. 20.0 for 20%) or loyalty tier."""
    if isinstance(discount, str):
        discount_pct = TIER_DISCOUNTS.get(discount.lower(), 0.0)
    else:
        discount_pct = float(discount)
    return price * (discount_pct / 100.0)
