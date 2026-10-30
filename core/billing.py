def calculate_discount(price: float, discount_pct: float) -> float:
    """Calculate discount amount from an explicit percentage (e.g. 20.0 for 20%)."""
    return price * (discount_pct / 100.0)
