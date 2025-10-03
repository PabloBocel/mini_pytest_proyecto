from typing import Iterable, Dict
from pathlib import Path
import csv

def persist_order(items: Iterable[Dict], total: float, outfile: str | Path) -> Path:
    path = Path(outfile)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "price", "qty"])
        for it in items:
            writer.writerow([it["name"], float(it["price"]), int(it.get("qty", 1))])
        writer.writerow([])
        writer.writerow(["TOTAL", total, ""])
    return path
