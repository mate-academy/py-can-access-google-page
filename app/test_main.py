import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, connection, expected",
    [
        pytest.param(
            False, False, "Not accessible", id="Check your URL and connection"
        ),
        pytest.param(
            True, False, "Not accessible", id="Check your URL"
        ),
        pytest.param(
            False, True, "Not accessible", id="Check your connection"
        ),
        pytest.param(
            True, True, "Accessible", id="Your URL and connection are fine"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_url: mock.Mock,
        mock_connection: mock.Mock,
        valid_url: bool,
        connection: bool,
        expected: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_connection.return_value = connection
    assert can_access_google_page("www.mate.academy.com") == expected
