def test_stock_cannot_go_negative(client, auth_header):
    client.post("/stock/adjust", json={
        "product_id": 1,
        "location_id": 1,
        "quantity": 10,
        "movement_type": "IN"
    }, headers=auth_header)

    res = client.post("/stock/adjust", json={
        "product_id": 1,
        "location_id": 1,
        "quantity": 50,
        "movement_type": "OUT"
    }, headers=auth_header)

    assert res.status_code == 400

