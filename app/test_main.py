from app.main import can_access_google_page
from typing import Any


def test_can_access_google_page_accessible(mocker: Any) -> None:
    url = "https://www.google.com"

    mocker.patch("main.valid_google_url", return_value=True)
    mocker.patch("main.has_internet_connection", return_value=True)

    result = can_access_google_page(url)

    assert result == "Accessible"


def test_can_access_google_page_not_accessible_due_to_url(
        mocker: Any
) -> None:
    url = "https://www.smth-incorrect.com"

    mocker.patch("main.valid_google_url", return_value=False)
    mocker.patch("main.has_internet_connection", return_value=True)

    result = can_access_google_page(url)

    assert result == "Not accessible"
