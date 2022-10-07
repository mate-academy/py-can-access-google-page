from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_page(
        mocked_valid_url: None,
        mocked_internet: None) -> None:
    mocked_valid_url.return_value = True
    mocked_internet.return_value = True

    assert can_access_google_page("some url") == "Accessible", (
        "Should return 'Accessible' if url is valid and "
        "internet connection available"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url(
        mocked_valid_url: None,
        mocked_internet: None) -> None:
    mocked_valid_url.return_value = False
    mocked_internet.return_value = True

    assert can_access_google_page("some url") == "Not accessible", (
        "Should return 'Not accessible' if url is invalid!"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_connection(
        mocked_valid_url: None,
        mocked_internet: None) -> None:
    mocked_valid_url.return_value = True
    mocked_internet.return_value = False

    assert can_access_google_page("some url") == "Not accessible", (
        "Should return 'Not accessible' if internet connection is missing"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_connection_and_url_is_invalid(
        mocked_valid_url: None,
        mocked_internet: None
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet.return_value = False

    assert can_access_google_page("some url") == "Not accessible", (
        "Should return 'Not accessible' if internet "
        "connection is missing and url is invalid"
    )
