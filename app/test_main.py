import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,connection,valid_url,expected",
    [
        pytest.param(
            "https://wikipedia.org/wiki/", True, False, "Not accessible",
            id="cannot connection to url"
        ),
        pytest.param(
            "https://wikipedia.org/wiki/", False, True, "Not accessible",
            id="url isn't valid"
        ),
        pytest.param(
            "https://wikipedia.org/wiki/", True, True, "Accessible",
            id="url valid and connection success"
        ),
        pytest.param(
            "https://wikipedia.org/wiki/", False, False, "Not accessible",
            id="cannot connection to url and url isn't valid"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google(
        mock_connection: mock,
        mock_valid_url: mock,
        url: str,
        connection: bool,
        valid_url: bool,
        expected: str,
):
    mock_connection.return_value = connection
    mock_valid_url.return_value = valid_url
    assert can_access_google_page(url) == expected
