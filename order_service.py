from math_utils import calculate_tax

def process_order(price: float) -> float:
    tax = calculate_tax(price)
    return price + tax
