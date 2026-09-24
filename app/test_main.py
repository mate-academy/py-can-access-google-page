from app.main import can_access_google_page

from pytest_mock import MockerFixture


def test_can_access_google_page_valid_url_and_connection(
        mocker: MockerFixture) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


def test_can_access_google_page_invalid_url(mocker: MockerFixture) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


def test_can_access_google_page_no_internet_connection(
        mocker: MockerFixture) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


def test_can_access_google_page_invalid_url_and_no_connection(
        mocker: MockerFixture) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"
