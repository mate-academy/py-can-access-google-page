import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_param_valid_google_url, mock_param_internet_connection, result",
    [pytest.param(True, True, "Accessible",
                  id="Test when URL and Connection is valid"),
     pytest.param(True, False, "Not accessible",
                  id="Test when URL is valid and Connection is invalid"),
     pytest.param(False, True, "Not accessible",
                  id="Test when URL is invalid and Connection is valid"),
     pytest.param(False, False, "Not accessible",
                  id="Test when URL is invalid and Connection is invalid")
     ])
def test_can_access_google_page(mock_param_valid_google_url: bool,
                                mock_param_internet_connection: bool,
                                result: str) -> None:
    with (mock.patch("app.main.valid_google_url") as
          mock_func_valid_google_url):
        mock_func_valid_google_url.return_value = mock_param_valid_google_url
        with (mock.patch("app.main.has_internet_connection")
              as mock_func_int_connect):
            mock_func_int_connect.return_value = mock_param_internet_connection
            if (mock_param_valid_google_url is True
                    and mock_param_internet_connection is True):
                assert can_access_google_page("Url") == result
            else:
                assert can_access_google_page("Url") == result
