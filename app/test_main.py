# write your code here
import pytest
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url_validity, internet_connection, output",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Should return 'Accessible' if validity and connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Should return 'Not accessible if no connection'"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Should return 'Not accessible' if no valid url"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Should return 'Not accessible' if no valid url and connection"
        )
    ]
)
def test_can_access_google_page(
        mock_valid_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
        url_validity: bool,
        internet_connection: bool,
        output: str
) -> None:
    mock_valid_url.return_value = url_validity
    mock_has_internet_connection.return_value = internet_connection

    assert can_access_google_page("https://google.com") == output
