import datetime
from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page(
        mock_internet: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_function_was_called(
        mock_internet: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    url = "http$://www.g00g1e.c0m"

    can_access_google_page(url)

    mock_valid.assert_called_once_with(url)


@pytest.mark.parametrize("hour,expected", [
    (3, "Not accessible"),
    (6, "Accessible"),
    (12, "Accessible"),
    (22, "Accessible"),
    (23, "Not accessible"),
])
@mock.patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_hours(
        mock_valid: mock.MagicMock,
        hour: int,
        expected: str
) -> None:
    class FakeDatetime(datetime.datetime):
        @classmethod
        def now(cls) -> datetime.datetime:
            return cls(2023, 1, 1, hour, 0, 0)

    with mock.patch("app.main.datetime.datetime", FakeDatetime):
        assert can_access_google_page("https://www.google.com") == expected
