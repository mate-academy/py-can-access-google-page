import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, result",
    [
        ("https://www.google.com/", "Accessible"),
        ("https://www.gogle.com/", "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_right_time(
        mocked_internet: callable,
        mocked_validator: callable,
        url: str,
        result: str) -> None:

    mocked_internet.return_value = True

    assert(
        can_access_google_page(url) == result
    )

    mocked_validator.assert_called_once_with(url)
    mocked_internet.assert_called_once()


@pytest.mark.parametrize(
    "url, result",
    [
        ("https://www.google.com/", "Not accessible"),
        ("https://www.gogle.com/", "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_wrong_time(
        mocked_internet: callable,
        mocked_validator: callable,
        url: str,
        result: str) -> None:

    mocked_internet.return_value = False

    assert(
        can_access_google_page(url) == result
    )

    mocked_validator.assert_called_once_with(url)
    mocked_internet.assert_called_once()
