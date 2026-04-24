from unittest.mock import patch

from app.main import can_access_google_page


def test_can_access_google_and_internet_connection_true() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page("correct url") == "Accessible"


def test_can_access_google_true_has_internet_false() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page("correct url") == "Not accessible"


def test_can_access_google_false_has_internet_true() -> None:
    with patch("app.main.valid_google_url", return_value=False):
        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page("incorrect url") == "Not accessible"


def test_can_access_google_false_has_internet_false() -> None:
    with patch("app.main.valid_google_url", return_value=False):
        with patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page("incorrect url") == "Not accessible"
