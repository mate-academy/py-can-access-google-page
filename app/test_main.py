from unittest.mock import patch
from app.main import can_access_google_page


def test_should_access_google_page_when_url_valid_and_has_internet() -> None:
    with (patch("app.main.valid_google_url", return_value=True,),
          patch("app.main.has_internet_connection", return_value=True,)):
        assert can_access_google_page("some_url") == "Accessible"


def test_should_access_google_page_when_url_valid_and_no_internet() -> None:
    with (patch("app.main.valid_google_url", return_value=True,),
          patch("app.main.has_internet_connection", return_value=False,)):
        assert can_access_google_page("some_url") == "Not accessible"


def test_should_access_google_page_when_url_invalid() -> None:
    with patch("app.main.valid_google_url", return_value=False,):
        assert can_access_google_page("some_url") == "Not accessible"
