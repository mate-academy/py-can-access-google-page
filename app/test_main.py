from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "mock_internet, mock_valid, expected",
    [
        (
            True,
            True,
            "Accessible",
        ),
        (
            False,
            True,
            "Not accessible",
        ),
        (
            True,
            False,
            "Not accessible",
        ),
        (
            False,
            False,
            "Not accessible",
        ),
    ],
    ids=[
        "internet and valid url",
        "no internet",
        "invalid url",
        "no internet and invalid url",
    ]
)
def test_can_access_google_page(
                                mock_has_internet_connection: mock.Mock,
                                mock_valid_google_url: mock.Mock,
                                mock_internet: bool,
                                mock_valid: bool,
                                expected: str
) -> None:
    mock_has_internet_connection.return_value = mock_internet
    mock_valid_google_url.return_value = mock_valid
    assert can_access_google_page("https://www.google.com") == expected
