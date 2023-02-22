from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, mock_internet, mock_valid, expected",
    [
        (
            "https://www.google.com",
            True,
            True,
            "Accessible",
        ),
        (
            "https://www.google.com",
            False,
            True,
            "Not accessible",
        ),
        (
            "https://www.google.com",
            True,
            False,
            "Not accessible",
        ),
        (
            "https://www.google.com",
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
def test_can_access_google_page(url: str,
                                mock_internet: bool,
                                mock_valid: bool,
                                expected: str) -> None:
    with mock.patch("app.main.valid_google_url", return_value=mock_valid):
        with mock.patch("app.main.has_internet_connection",
                        return_value=mock_internet):
            assert can_access_google_page(url) == expected
