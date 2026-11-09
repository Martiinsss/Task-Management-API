def test_create_and_list_own_tasks(client, make_user):
    headers = make_user()

    created = client.post("/tasks/", json={"title": "Write tests"}, headers=headers)
    listed = client.get("/tasks/", headers=headers)

    assert created.status_code == 200
    assert created.json()["title"] == "Write tests"
    assert [task["title"] for task in listed.json()] == ["Write tests"]


def test_user_cannot_see_other_users_tasks(client, make_user):
    alice = make_user("alice@example.com")
    bob = make_user("bob@example.com")
    client.post("/tasks/", json={"title": "Alice's task"}, headers=alice)

    response = client.get("/tasks/", headers=bob)

    assert response.status_code == 200
    assert response.json() == []


def test_user_cannot_delete_other_users_task(client, make_user):
    alice = make_user("alice@example.com")
    bob = make_user("bob@example.com")
    task_id = client.post("/tasks/", json={"title": "Alice's task"}, headers=alice).json()["id"]

    response = client.delete(f"/tasks/{task_id}", headers=bob)

    assert response.status_code == 403
    assert len(client.get("/tasks/", headers=alice).json()) == 1


def test_owner_can_delete_task(client, make_user):
    headers = make_user()
    task_id = client.post("/tasks/", json={"title": "Temporary"}, headers=headers).json()["id"]

    response = client.delete(f"/tasks/{task_id}", headers=headers)

    assert response.status_code == 200
    assert client.get("/tasks/", headers=headers).json() == []


def test_delete_missing_task_returns_404(client, make_user):
    headers = make_user()

    response = client.delete("/tasks/9999", headers=headers)

    assert response.status_code == 404
