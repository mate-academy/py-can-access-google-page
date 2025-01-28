import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.fixture()
def url_template() -> str:
    url = "http://www.google.com"
    return url


def test_page_accessible(url_template: str) -> None:
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=True):

        result = can_access_google_page(url_template)

        assert result == "Accessible"


def test_page_not_accessible_invalid_url(url_template: str) -> None:
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=True):

        result = can_access_google_page(url_template)

        assert result == "Not accessible"


def test_page_not_accessible_no_internet(url_template: str) -> None:
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=False):

        result = can_access_google_page(url_template)

        assert result == "Not accessible"


def test_page_not_accessible_invalid_url_and_no_internet(url_template: str
                                                         ) -> None:
    with patch("app.main.valid_google_url", return_value=False), \
         patch("app.main.has_internet_connection", return_value=False):

        result = can_access_google_page(url_template)

        assert result == "Not accessible"
