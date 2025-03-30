from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_has_internet,"
    " mock_valid_google,"
    " expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Internet connection is available and URL is valid"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Internet connection is not available"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="URL is not valid"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Internet connection is not available and URL is not valid"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: mock.Mock,
    mock_valid_google_url: mock.Mock,
    mock_has_internet: bool,
    mock_valid_google: bool,
    expected_result: str
) -> None:
    mock_has_internet_connection.return_value = mock_has_internet
    mock_valid_google_url.return_value = mock_valid_google
    url = "http://www.google.com"
    assert can_access_google_page(url) == expected_result
