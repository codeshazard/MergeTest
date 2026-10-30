from core.billing import calculate_discount


def calculate_total(price: float, user_tier: str) -> float:
    """Compute the final payable total after applying tier discounts."""
    discount = calculate_discount(price, user_tier)
    return round(price - discount, 2)
