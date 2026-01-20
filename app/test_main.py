from unittest import mock

import pytest

from app.main import can_access_google_page


def test_can_if_functions_called_once() -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mock_internet_connection,
          mock.patch("app.main.valid_google_url") as mock_valid_url):

        can_access_google_page("https://www.youtube.com/")
        mock_internet_connection.assert_called_once()
        mock_valid_url.assert_called_once_with("https://www.youtube.com/")

    assert can_access_google_page("https://www.youtube.com/") == "Accessible"


@pytest.mark.parametrize(
    "bool1, bool2, result",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_different_cases(bool1: bool, bool2: bool, result: str) -> None:
    with (mock.patch("app.main.has_internet_connection", return_value=bool1),
          mock.patch("app.main.valid_google_url", return_value=bool2)):
        assert can_access_google_page("https://www.youtube.com/") == result
