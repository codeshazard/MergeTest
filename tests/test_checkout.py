import pytest
from services.checkout import calculate_total


def test_gold_tier_checkout():
    # 100.0 with 20% discount should be 80.0
    assert calculate_total(100.0, "gold") == 80.0


def test_silver_tier_checkout():
    # 100.0 with 10% discount should be 90.0
    assert calculate_total(100.0, "silver") == 90.0


def test_regular_tier_checkout():
    # Default user gets 0% discount
    assert calculate_total(100.0, "regular") == 100.0
