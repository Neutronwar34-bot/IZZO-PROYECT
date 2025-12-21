def test_create_product(client, auth_header):
    res = client.post("/products/", json={
        "sku": "SKU-001",
        "name": "Test Product",
        "price": 10.5,
        "category_id": 1
    }, headers=auth_header)

    assert res.status_code == 201

