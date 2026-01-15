from unittest.mock import patch

import app.main as main


def test_accessible_when_connection_and_valid_url() -> None:
    url: str = "https://www.google.com"

    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):

        result: str = main.can_access_google_page(url)

        assert result == "Accessible"


def test_not_accessible_when_only_connection_is_true() -> None:
    url: str = "https://www.google.com"

    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):

        result: str = main.can_access_google_page(url)

        assert result == "Not accessible"


def test_not_accessible_when_only_valid_url_is_true() -> None:
    url: str = "https://www.google.com"

    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):

        result: str = main.can_access_google_page(url)

        assert result == "Not accessible"


def test_not_accessible_when_both_are_false() -> None:
    url: str = "https://www.google.com"

    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=False):

        result: str = main.can_access_google_page(url)

        assert result == "Not accessible"
