import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_url_valid,mock_internet,expected_value",
    [
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Test invalid url and no internet"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Test no internet"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Test invalid url"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="Test valid url and have internet"
        ),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_internet_connection: object,
    mock_valid_url_function: object,
    mock_url_valid: bool,
    mock_internet: bool,
    expected_value: str
) -> None:
    mock_internet_connection.return_value = mock_internet
    mock_valid_url_function.return_value = mock_url_valid
    assert can_access_google_page("https://www.google.com") == expected_value
