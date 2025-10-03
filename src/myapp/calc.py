from typing import Iterable, Dict

def compute_total(items: Iterable[Dict[str, float]], tax_rate: float) -> float:
    """
    Calcula el total con impuesto.
    items: iterable de dicts con claves {"name": str, "price": float, "qty": int}
    tax_rate: tasa de impuesto en [0,1], p.ej. 0.12 para 12%
    """
    subtotal = 0.0
    for it in items:
        price = float(it["price"])
        qty = int(it.get("qty", 1))
        subtotal += price * qty
    total = round(subtotal * (1.0 + tax_rate), 2)
    return total
