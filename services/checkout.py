from core.billing import calculate_discount, TIER_DISCOUNTS

def calculate_total(price: float, user_tier: str) -> float:
    """Compute the final payable total after applying tier discounts."""
    discount_pct = TIER_DISCOUNTS.get(user_tier.lower(), 0.0)
    discount = calculate_discount(price, discount_pct)
    return round(price - discount, 2)
