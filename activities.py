import requests

# import jsonpath
# import json


base_url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/"


def test_get_activities():
    assert requests.get(base_url).status_code == 200


def test_post_activities():
    request_json = {
        "id": 0,
        "title": "string",
        "dueDate": "2023-03-22T13:14:29.918Z",
        "completed": True
    }
    assert requests.post(base_url, json=request_json).status_code == 200


def test_get_an_activity():
    endpoint = "1"
    assert requests.get(base_url + endpoint).status_code == 200


def test_put_an_activity():
    endpoint = "1"
    request_json = {
        "id": 1,
        "title": "string",
        "dueDate": "2023-03-22T13:14:29.918Z",
        "completed": True
    }
    assert requests.put(base_url + endpoint, json=request_json)


def test_delete_an_activity():
    endpoint = "1"
    assert requests.delete(base_url + endpoint).status_code == 200
