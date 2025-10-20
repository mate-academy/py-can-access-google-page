from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
    mocked_url_validator: mock.MagicMock,
    mocked_internet_connection: mock.MagicMock
) -> None:
    url = "www.google.com/"

    mocked_url_validator.return_value = True
    mocked_internet_connection.return_value = True

    can_access_google_page(url)

    mocked_url_validator.assert_called_once_with(url)
    mocked_internet_connection.assert_called_once()

    assert can_access_google_page(url) == "Accessible"


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected_result",
    [
        pytest.param(True, False, "Not accessible", id="TF"),
        pytest.param(False, True, "Not accessible", id="FT"),
        pytest.param(True, True, "Accessible", id="TT"),
        pytest.param(False, False, "Not accessible", id="FF"),
    ],
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_by_bool(
    mocked_valid_google_url: mock.MagicMock,
    mocked_has_internet_connection: mock.MagicMock,
    valid_google_url: bool,
    has_internet_connection: bool,
    expected_result: str,
) -> None:
    url = "www.google.com/"

    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection

    result = can_access_google_page(url)

    if has_internet_connection:
        mocked_valid_google_url.assert_called_once_with(url)
    else:
        mocked_valid_google_url.assert_not_called()

    assert result == expected_result
