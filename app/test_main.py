from pytest_mock import MockerFixture

from app.main import can_access_google_page


def test_accessible_when_url_valid_and_connection_exists(
    mocker: MockerFixture,
) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=True)

    assert can_access_google_page("https://google.com") == "Accessible"


def test_not_accessible_if_url_is_not_valid(
    mocker: MockerFixture,
) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=True)

    assert can_access_google_page("https://google.com") == "Not accessible"


def test_not_accessible_if_no_internet_connection(
    mocker: MockerFixture,
) -> None:
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=False)

    assert can_access_google_page("https://google.com") == "Not accessible"


def test_not_accessible_if_url_invalid_and_no_connection(
    mocker: MockerFixture,
) -> None:
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=False)

    assert can_access_google_page("https://google.com") == "Not accessible"
