import pytest
import requests
from sentiment import DualAnalyzer

@pytest.mark.parametrize("url", [
    "https://apnews.com/hub/business",
    "https://www.ksdk.com/money",
])
def test_url_connection_success(url): #all this function does is test if the URL is getting a valid response when requested.
    try:
        response = requests.get(url, timeout=5)
        assert response.status_code == 200
    except requests.RequestException as e:
        pytest.fail(f"Connection failed for {url}: {e}")


def test_analyzer_initializes():
    analyzer = DualAnalyzer()
    assert hasattr(analyzer, "analyze_phi"), "analyze_phi function missing from Dual Analyzer class"
    assert hasattr(analyzer, "analyze_llama"), "analyze_llama missing from Dual Analyzer class"
