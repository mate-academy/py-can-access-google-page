from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "url_is_valid, internet_exists, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_depends_on_valid_url_and_internet_connection(
    mocked_valid_url: mock.MagicMock,
    mocked_internet: mock.MagicMock,
    url_is_valid: bool,
    internet_exists: bool,
    expected_result: str,
) -> None:
    mocked_valid_url.return_value = url_is_valid
    mocked_internet.return_value = internet_exists

    result = main.can_access_google_page("https://www.google.com")

    assert result == expected_result


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_google_url_is_called_with_given_url(
    mocked_valid_url: mock.MagicMock,
    mocked_internet: mock.MagicMock,
) -> None:
    mocked_valid_url.return_value = True
    mocked_internet.return_value = True
    url = "https://www.google.com"

    main.can_access_google_page(url)

    mocked_valid_url.assert_called_once_with(url)
