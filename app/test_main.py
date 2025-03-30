from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_right_time(
        mocked_internet: callable,
        mocked_validator: callable,
        url: str = "some.cite") -> None:

    mocked_internet.return_value = True
    mocked_validator.return_value = True

    assert (
        can_access_google_page(url) == "Accessible"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_not_access_google_page_wrong_time(
        mocked_internet: callable,
        mocked_validator: callable,
        url: str = "some.cite") -> None:

    mocked_internet.return_value = True
    mocked_validator.return_value = False

    assert (
        can_access_google_page(url) == "Not accessible"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_not_access_google_page_wrong_cite(
        mocked_internet: callable,
        mocked_validator: callable,
        url: str = "some.cite") -> None:

    mocked_internet.return_value = False
    mocked_validator.return_value = True

    assert (
        can_access_google_page(url) == "Not accessible"
    )
