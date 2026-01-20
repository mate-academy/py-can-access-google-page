import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, google_url, result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="valid to access the Google and it has internet connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="not valid to access the Google home page"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="no internet connection"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_has_internet_connection,
        mock_valid_google_url,
        internet_connection,
        google_url,
        result
):
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = google_url
    assert can_access_google_page("google.com") == result
