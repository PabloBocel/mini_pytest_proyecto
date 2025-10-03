import pytest
from myapp.calc import compute_total

def test_compute_total_basic():
    items = [{"name":"A", "price":10, "qty":2}, {"name":"B", "price":5, "qty":1}]
    assert compute_total(items, 0.0) == 25.00
    assert compute_total(items, 0.12) == 28.00

@pytest.mark.parametrize("tax_rate,expected", [(0.0, 10.00), (0.5, 15.00), (1.0, 20.00)])
def test_compute_total_parametrized(tax_rate, expected):
    items = [{"name":"X", "price":10, "qty":1}]
    assert compute_total(items, tax_rate) == expected
