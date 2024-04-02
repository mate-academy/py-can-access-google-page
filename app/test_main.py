import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_functions() -> tuple:
    with (mock.patch("app.main.valid_google_url") as mock_valid_google,
          mock.patch("app.main.has_internet_connection")
            as mock_has_internet_connection):
        yield mock_valid_google, mock_has_internet_connection


@pytest.mark.parametrize("valid_google, has_inet_connection, result",
                         [(False, False, "Not accessible"),
                          (False, True, "Not accessible"),
                          (True, False, "Not accessible"),
                          (True, True, "Accessible")])
def test_can_access_google_page_universal(mock_functions: tuple,
                                          valid_google: bool,
                                          has_inet_connection: bool,
                                          result: str) -> None:
    mock_valid_google, mock_has_internet_connection = mock_functions
    mock_valid_google.return_value = valid_google
    mock_has_internet_connection.return_value = has_inet_connection
    resulto = can_access_google_page("/1")
    assert resulto == result
