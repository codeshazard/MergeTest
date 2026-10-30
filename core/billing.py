def calculate_discount(price: float, user_tier: str) -> float:
    """Calculate discount amount based on user loyalty tier."""
    tiers = {
        "gold": 0.20,
        "silver": 0.10,
        "bronze": 0.05,
    }
    rate = tiers.get(user_tier.lower(), 0.0)
    return price * rate
