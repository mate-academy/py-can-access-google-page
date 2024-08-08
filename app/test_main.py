from pytest_mock import MockerFixture
from app.main import can_access_google_page


def test_can_access_google_page_accessible(
        mocker: MockerFixture
) -> None:
    mocker.patch("app.main.has_internet_connection", return_value=True)
    mocker.patch("app.main.valid_google_url", return_value=True)

    result = can_access_google_page("http://www.google.com")
    assert result == "Accessible"


def test_can_access_google_page_not_accessible_no_internet(
        mocker: MockerFixture
) -> None:
    mocker.patch("app.main.has_internet_connection", return_value=False)
    mocker.patch("app.main.valid_google_url", return_value=True)

    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"


def test_can_access_google_page_not_accessible_invalid_url(
        mocker: MockerFixture
) -> None:
    mocker.patch("app.main.has_internet_connection", return_value=True)
    mocker.patch("app.main.valid_google_url", return_value=False)

    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"
