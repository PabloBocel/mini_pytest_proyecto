from myapp.action import persist_order

def test_persist_order_writes_csv(tmp_path):
    items = [{"name":"A","price":2.5,"qty":2},{"name":"B","price":1.0,"qty":1}]
    total = 6.0
    outfile = tmp_path / "order.csv"
    path = persist_order(items, total, outfile)
    content = path.read_text(encoding="utf-8").replace("\r\n","\n")
    assert "A,2.5,2" in content
    assert "B,1.0,1" in content
    assert "TOTAL,6.0," in content
