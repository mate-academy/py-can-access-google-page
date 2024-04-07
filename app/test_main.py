from typing import Any

from app.main import can_access_google_page


def test_can_access_google_page(mocker: Any) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=True)

    assert can_access_google_page("https://www.google.com") == "Accessible"

    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("https://invalidurl.com") == "Not accessible"
