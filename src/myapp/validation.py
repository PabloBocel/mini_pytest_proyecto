from typing import Iterable, Dict

class ValidationError(ValueError):
    pass

def validate_items(items: Iterable[Dict]) -> None:
    for idx, it in enumerate(items):
        if not it.get("name"):
            raise ValidationError(f"item[{idx}].name vacío")
        price = it.get("price")
        if price is None or float(price) < 0:
            raise ValidationError(f"item[{idx}].price inválido")
        qty = int(it.get("qty", 1))
        if qty < 1:
            raise ValidationError(f"item[{idx}].qty debe ser >= 1")

def validate_tax_rate(tax_rate: float) -> None:
    if not (0.0 <= float(tax_rate) <= 1.0):
        raise ValidationError("tax_rate debe estar en [0,1]")
