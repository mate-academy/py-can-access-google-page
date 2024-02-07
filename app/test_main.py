import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, correct_url, connection_exists, expected_result",
    [
        pytest.param("https://www.google.com", True, True, "Accessible",
                     id="return Accessible if url valid and allowable time"),
        pytest.param("invalid_url", False, True, "Not accessible",
                     id="return Not accessible if got invalid url"),
        pytest.param("https://www.google.com", True, False, "Not accessible",
                     id="return Not accessible if time is not allowable"),
        pytest.param("invalid_url", False, False, "Not accessible",
                     id="return Not accessible if time is not allowable "
                        "and if url is invalid"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: mock,
        mock_has_internet_connection: mock,
        url: str,
        correct_url: bool,
        connection_exists: bool,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = correct_url
    mock_has_internet_connection.return_value = connection_exists
    result = can_access_google_page(url)
    assert result == expected_result
