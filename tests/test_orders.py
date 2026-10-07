import pytest
 
from src.orders import Order, calculate_order_total
 
 
def test_calculate_order_total_matches_original() -> None:
    sample_order: Order = {
        "items": [
            {"price": 25.0, "qty": 2},
            {"price": 40.0, "qty": 1},
            {"price": -5.0, "qty": 3},
        ],
        "member": True,
        "country": "PK",
    }
    assert calculate_order_total(sample_order) == pytest.approx(86.0)
