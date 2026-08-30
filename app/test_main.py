import pytest
from unittest.mock import patch, MagicMock


from app import main


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "connection,google,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        mocked_internet_connection: MagicMock,
        mocked_google: MagicMock,
        connection: bool,
        google: bool,
        result: str
) -> None:
    mocked_internet_connection.return_value = connection
    mocked_google.return_value = google
    assert main.can_access_google_page("https://www.google.com") == result
