from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with mock.patch(
            "app.main.valid_google_url", return_value=True
    ), mock.patch(
        "app.main.has_internet_connection", return_value=True
    ):
        url = "https://google.com"
        assert can_access_google_page(url) == "Accessible"


def test_can_not_access_google_page() -> None:
    with mock.patch(
            "app.main.valid_google_url", return_value=False
    ), mock.patch(
        "app.main.has_internet_connection", return_value=False
    ):
        url = "https://google.com"
        assert can_access_google_page(url) == "Not accessible"


def test_can_nt_access_google_page() -> None:
    with mock.patch(
            "app.main.valid_google_url", return_value=True
    ), mock.patch(
        "app.main.has_internet_connection", return_value=False
    ):
        url = "https://google.com"
        assert can_access_google_page(url) == "Not accessible"


def test_can_n_access_google_page() -> None:
    with mock.patch(
            "app.main.valid_google_url", return_value=False
    ), mock.patch(
        "app.main.has_internet_connection", return_value=True
    ):
        url = "https://google.com"
        assert can_access_google_page(url) == "Not accessible"
