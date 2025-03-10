import requests

def test_get_users_list():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    
    data = response.json()
    assert "page" in data, "Ключ 'page' отсутствует в ответе"
    assert "data" in data, "Ключ 'data' отсутствует в ответе"
    assert isinstance(data["data"], list), "Данные пользователей должны быть списком"

def test_get_single_user():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)

    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

    data = response.json()
    assert "data" in data, "Ключ 'data' отсутствует в ответе"
    assert data["data"]["id"] == 2, "ID пользователя не соответствует ожидаемому"

def test_create_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "John",
        "job": "QA"
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 201, f"Ожидался статус-код 201, но получен {response.status_code}"

    data = response.json()
    assert "name" in data, "Ключ 'name' отсутствует в ответе"
    assert "job" in data, "Ключ 'job' отсутствует в ответе"
    assert data["name"] == payload["name"], "Имя пользователя не соответствует ожидаемому"
    assert data["job"] == payload["job"], "Должность пользователя не соответствует ожидаемой"

def test_update_user():
    url = "https://reqres.in/api/users/2"
    payload = {
        "name": "John",
        "job": "Lead QA"
    }
    response = requests.put(url, json=payload)

    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

    data = response.json()
    assert "name" in data, "Ключ 'name' отсутствует в ответе"
    assert "job" in data, "Ключ 'job' отсутствует в ответе"
    assert data["name"] == payload["name"], "Имя пользователя не обновлено"
    assert data["job"] == payload["job"], "Должность пользователя не обновлена" 

def test_delete_user():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url)

    assert response.status_code == 204, f"Ожидался статус-код 204, но получен {response.status_code}"


def test_login():
    url = "https://reqres.in/api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

    data = response.json()
    assert "token" in data, "Ключ 'token' отсутствует в ответе"