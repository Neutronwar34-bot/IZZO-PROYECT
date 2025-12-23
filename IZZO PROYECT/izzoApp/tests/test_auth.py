def test_register_and_login(client):
    # Register
    res = client.post("/auth/register", json={
        "email": "admin@test.com",
        "password": "123456",
        "role": "admin"
    })
    #assert res.status_code == 201
    print("REGISTER:", res.status_code, res.json)
    # Login
    #res = client.post("/auth/login", json={
    #    "email": "admin@test.com",
    #    "password": "123456"
    #})

#    data = res.get_json()
 #   assert "token" in data
