from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def url() -> None:
    return "https://www.google.com/"


@pytest.fixture
def mock_internet() -> mock.MagicMock:
    with (mock.patch("app.main.has_internet_connection")
          as mock_internet_connection):
        yield mock_internet_connection


@pytest.fixture
def mock_url_valid() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


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
def test_success_cases(
        mock_internet: mock.MagicMock,
        mock_url_valid: mock.MagicMock,
        url: str,
        has_internet: bool,
        has_valid_url: bool,
        expected: str
) -> None:
    mock_url_valid.return_value = has_valid_url
    mock_internet.return_value = has_internet

    assert can_access_google_page(url) == expected


def test_func_callable(
        mock_internet: mock.MagicMock,
        mock_url_valid: mock.MagicMock,
        url: str
) -> None:
    can_access_google_page(url)

    mock_internet.assert_called_once()
    mock_url_valid.assert_called_once_with(url)
