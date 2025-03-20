import pytest
import app.main as ap
from unittest.mock import patch


@pytest.fixture()
def url_template() -> str:
    return "https://google.com"


test_url_method = "app.main.valid_google_url"
test_internet_connection_method = "app.main.has_internet_connection"


def test_valid_url_and_connection_exists(url_template: str) -> None:
    with patch(test_url_method, return_value=True), \
            patch(test_internet_connection_method, return_value=True):
        assert ap.can_access_google_page(url_template) == "Accessible"


def test_invalid_url_and_connection_exists(url_template: str) -> None:
    with patch(test_url_method, return_value=False), \
            patch(test_internet_connection_method, return_value=True):
        assert ap.can_access_google_page(url_template) == "Not accessible"


def test_valid_url_and_no_connection(url_template: str) -> None:
    with patch(test_url_method, return_value=True), \
            patch(test_internet_connection_method, return_value=False):
        assert ap.can_access_google_page(url_template) == "Not accessible"


def test_invalid_url_and_no_connection(url_template: str) -> None:
    with patch(test_url_method, return_value=False), \
            patch(test_internet_connection_method, return_value=False):
        assert ap.can_access_google_page(url_template) == "Not accessible"
