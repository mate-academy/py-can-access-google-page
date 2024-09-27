from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_accessible(
    valid_url: mock, has_inet: mock
) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_not_accessible_no_inet(
    valid_url: mock, has_inet: mock
) -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_not_accessible_invalid_url(
    valid_url: mock, has_inet: mock
) -> None:
    assert can_access_google_page("https://www&!?sA.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_not_accessible_no_inet_and_invalid_url(
    valid_url: mock, has_inet: mock
) -> None:
    assert can_access_google_page("https://www&!?sA.com") == "Not accessible"
