import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize("arg1 , arg2, expected",
                         [
                             (True, True, "Accessible"),
                             (True, False, "Not accessible"),
                             (False, True, "Not accessible"),
                             (False, False, "Not accessible")
                         ]
                         )
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock,
        arg1: bool,
        arg2: bool,
        expected: bool) -> None:
    mock_has_internet_connection.return_value = arg1
    mock_valid_google_url.return_value = arg2
    assert (can_access_google_page("http//:googlecom") == expected)
