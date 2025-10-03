import pytest
from myapp.validation import validate_items, validate_tax_rate, ValidationError

def test_validate_items_ok():
    validate_items([{"name":"A","price":1.0,"qty":1}])

def test_validate_items_fail_price():
    with pytest.raises(ValidationError):
        validate_items([{"name":"A","price":-1.0,"qty":1}])

def test_validate_items_fail_qty():
    with pytest.raises(ValidationError):
        validate_items([{"name":"A","price":1.0,"qty":0}])

@pytest.mark.parametrize("rate", [-0.1, 1.1])
def test_validate_tax_rate_out_of_range(rate):
    with pytest.raises(ValidationError):
        validate_tax_rate(rate)

def test_validate_tax_rate_ok():
    validate_tax_rate(0.0)
    validate_tax_rate(0.5)
    validate_tax_rate(1.0)
