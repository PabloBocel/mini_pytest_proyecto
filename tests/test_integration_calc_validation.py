from myapp.calc import compute_total
from myapp.validation import validate_items, validate_tax_rate

def test_integration_calc_with_validation():
    items = [{"name":"A","price":10,"qty":3}]
    validate_items(items)
    validate_tax_rate(0.12)
    assert compute_total(items, 0.12) == 33.6
