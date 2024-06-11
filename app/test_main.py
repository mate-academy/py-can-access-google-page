import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Test can access google page"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Test invalid url"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Test no internet connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Test invalid url and no internet connection"
        )
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: callable,
        mocked_has_internet_connection: callable,
        valid_url: bool,
        internet_connection: bool,
        expected_result: bool
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com/") == expected_result
