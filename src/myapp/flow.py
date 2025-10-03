from typing import Iterable, Dict, Tuple
from .validation import validate_items, validate_tax_rate
from .calc import compute_total
from .action import persist_order
from pathlib import Path

def run_order_flow(items: Iterable[Dict], tax_rate: float, outfile: str | Path) -> Tuple[float, Path]:
    validate_items(items)
    validate_tax_rate(tax_rate)
    total = compute_total(items, tax_rate)
    path = persist_order(items, total, outfile)
    return total, path
