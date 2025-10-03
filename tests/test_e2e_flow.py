from myapp.flow import run_order_flow

def test_end_to_end_flow(tmp_path):
    items = [{"name":"A","price":10,"qty":2}, {"name":"B","price":5,"qty":1}]
    total, path = run_order_flow(items, 0.12, tmp_path / "pedido.csv")
    assert total == 28.00
    assert path.exists()
    text = path.read_text(encoding="utf-8").replace("\r\n","\n")
    assert "TOTAL,28.0," in text
