from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, has_valid_url, expected",
    [
        pytest.param(True, True, "Accessible",
                     id="Access google page"),
        pytest.param(True, False, "Not accessible",
                     id="Fail, not valid url"),
        pytest.param(False, True, "Not accessible",
                     id="Fail, has not internet"),
        pytest.param(False, False, "Not accessible",
                     id="Fail, you have not intern and incorrect url")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_success_cases(
        mock_valid_url: mock.MagicMock,
        mock_internet_connection: mock.MagicMock,
        has_internet: bool,
        has_valid_url: bool,
        expected: str
) -> None:
    mock_valid_url.return_value = has_valid_url
    mock_internet_connection.return_value = has_internet

    assert can_access_google_page("https://www.google.com/") == expected


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_func_callable(
        mock_valid_url: mock.MagicMock,
        mock_internet_connection: mock.MagicMock
) -> None:
    url = "https://www.google.com/"
    can_access_google_page(url)

    mock_internet_connection.assert_called_once()
    mock_valid_url.assert_called_once_with(url)

