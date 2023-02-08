import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected_result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "You cannot access page if only 'valid url' is True.",
        "You cannot access page if only 'connection' is True.",
        "You cannot access page if 'connection' and 'valid url' are False.",
        "You can access page if 'connection' and 'valid url' are True."
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page_function(
        mock_valid_url: callable,
        mock_has_connection: callable,
        valid_url: bool,
        has_connection: bool,
        expected_result: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_connection.return_value = has_connection
    assert can_access_google_page("https://www.google.com/") == expected_result
