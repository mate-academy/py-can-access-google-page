from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_accessible(
        google_url: mock,
        internet_connection: mock
) -> None:
    assert can_access_google_page(
        "https://www.google.com"
    ) == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_invalid_url(
        google_url: mock,
        internet_connection: mock
) -> None:
    assert can_access_google_page(
        "https://www.invalidurl.com"
    ) == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_not_accessible(
        google_url: mock,
        internet_connection: mock
) -> None:
    assert can_access_google_page(
        "https://www.google.com"
    ) == "Not accessible"
