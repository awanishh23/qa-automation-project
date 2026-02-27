import requests

def test_get_user():

    url = "https://httpbin.org/get"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, timeout=10)

    print("Status:", response.status_code)

    assert response.status_code == 200

    data = response.json()

    assert "url" in data