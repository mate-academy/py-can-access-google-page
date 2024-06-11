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
            id="Function should return `Not accessible` if url is"
               " not valid and no internet connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Function should return `Not accessible` if "
               "no internet connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Function should return `Not accessible` if url is not valid"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="Function should return `Accessible` if valid "
               "url and have internet connection"
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
