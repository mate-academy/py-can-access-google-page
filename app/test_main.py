from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_internet: callable,
        mocked_validator: callable
) -> None:
    mocked_internet.return_value = True
    mocked_validator.return_value = True
    assert (
        can_access_google_page("https://www.google.com/") == "Accessible"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_not_access_google_page_no_internet_connection(
        mocked_internet: callable,
        mocked_validator: callable,
) -> None:
    mocked_internet.return_value = False
    mocked_validator.return_value = True
    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_not_access_google_page_not_valid_site(
        mocked_internet: callable,
        mocked_validator: callable
) -> None:
    mocked_internet.return_value = True
    mocked_validator.return_value = False
    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )
