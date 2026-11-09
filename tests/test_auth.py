def test_register_returns_user_without_password(client):
    response = client.post("/register", json={"email": "a@example.com", "password": "secret123"})

    assert response.status_code == 200
    body = response.json()
    assert body["email"] == "a@example.com"
    assert "password" not in body
    assert "hashed_password" not in body


def test_register_duplicate_email_is_rejected(client):
    payload = {"email": "a@example.com", "password": "secret123"}
    client.post("/register", json=payload)

    response = client.post("/register", json=payload)

    assert response.status_code == 400


def test_login_returns_bearer_token(client):
    client.post("/register", json={"email": "a@example.com", "password": "secret123"})

    response = client.post("/login", data={"username": "a@example.com", "password": "secret123"})

    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]


def test_login_with_wrong_password_is_rejected(client):
    client.post("/register", json={"email": "a@example.com", "password": "secret123"})

    response = client.post("/login", data={"username": "a@example.com", "password": "wrong"})

    assert response.status_code == 400


def test_login_with_unknown_user_is_rejected(client):
    response = client.post("/login", data={"username": "nobody@example.com", "password": "x"})

    assert response.status_code == 400


def test_tasks_require_authentication(client):
    response = client.get("/tasks/")

    assert response.status_code == 401
