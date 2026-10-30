def calculate_tax(amount: float, currency: str) -> float:
    """Calculate tax with required currency parameter."""
    rates = {'USD': 0.15, 'EUR': 0.20, 'GBP': 0.22}
    return amount * rates.get(currency, 0.15)
