def test_register_user(test_client):
    response = test_client.post("/api/auth/register", json={
        "username": "testinguser",
        "email": "testing@example.com",
        "password": "123456"
    })

    assert response.status_code in [200, 201]

def test_login_user(test_client):
    response = test_client.post("/api/auth/login", json={
        "email": "testing@example.com",
        "password": "123456"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()