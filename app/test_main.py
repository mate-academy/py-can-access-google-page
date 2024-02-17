import pytest
from unittest.mock import MagicMock
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, has_internet_connection, valid_google_url, expected_result",
    [
        pytest.param(
            "https://www.google.com.ua/",
            True,
            True,
            "Accessible",
            id="should return 'Accessible' "
               "if has internet connection and url is valid"
        ),
        pytest.param(
            "https://www.google.com.ua/",
            False,
            True,
            "Not accessible",
            id="should return 'Not accessible' "
               "if has not internet connection but url is valid"
        ),
        pytest.param(
            "Avada Kedavra",
            True,
            False,
            "Not accessible",
            id="should return 'Not accessible' "
               "if has internet connection but url is not valid"
        ),
        pytest.param(
            "Avada Kedavra",
            False,
            False,
            "Not accessible",
            id="should return 'Not accessible' "
               "if has not internet connection and url is not valid"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_valid_google_url: MagicMock,
        mocked_has_internet_connection: MagicMock,
        url: str,
        has_internet_connection: bool,
        valid_google_url: bool,
        expected_result: str
) -> None:
    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection

    result = can_access_google_page(url)

    assert result == expected_result


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_functions_called(
        mocked_valid_google_url: MagicMock,
        mocked_has_internet_connection: MagicMock,
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True

    can_access_google_page("https://www.google.com.ua/")

    mocked_valid_google_url.assert_called_with("https://www.google.com.ua/")
    mocked_has_internet_connection.assert_called_once()
