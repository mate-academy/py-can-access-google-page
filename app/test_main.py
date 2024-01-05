from unittest import mock
import app.main


@mock.patch(
    "app.main.valid_google_url", mock.MagicMock(return_value=True)
)
@mock.patch(
    "app.main.has_internet_connection", mock.MagicMock(return_value=True)
)
def test_can_access_google_page_all_true() -> None:
    assert app.main.can_access_google_page(
        "google.com"
    ) == "Accessible"


@mock.patch(
    "app.main.valid_google_url", mock.MagicMock(return_value=False)
)
@mock.patch(
    "app.main.has_internet_connection", mock.MagicMock(return_value=True)
)
def test_can_access_google_page_url_false() -> None:
    assert app.main.can_access_google_page(
        "google.com"
    ) == "Not accessible"


@mock.patch(
    "app.main.valid_google_url", mock.MagicMock(return_value=True)
)
@mock.patch(
    "app.main.has_internet_connection", mock.MagicMock(return_value=False)
)
def test_can_access_google_page_internet_connection_false() -> None:
    assert app.main.can_access_google_page(
        "google.com"
    ) == "Not accessible"
