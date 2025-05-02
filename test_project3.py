import pytest
import requests

@pytest.mark.parametrize("url", [
    "https://apnews.com/hub/business",
    "https://www.ksdk.com/money",
])
def test_url_connection_success(url):
    try:
        response = requests.get(url, timeout=5)
        assert response.status_code == 200
    except requests.RequestException as e:
        pytest.fail(f"Connection failed for {url}: {e}")

