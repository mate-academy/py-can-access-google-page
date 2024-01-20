import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,valid_url,internet_connection,expected_output",
    [
        pytest.param(
            "https://www.google.com",
            True,
            False,
            "Not accessible",
            id="Should return 'Not Accessible' if don't have internet"
        ),
        pytest.param(
            "https://www.google.com",
            False,
            True,
            "Not accessible",
            id="Should return 'Not Accessible' if URL is not valid"
        ),
        pytest.param(
            "https://www.google.com",
            False,
            False,
            "Not accessible",
            id=("Should return 'Not Accessible' if don't have internet"
                " and URL is not valid")
        ),
        pytest.param(
            "https://www.google.com",
            True,
            True,
            "Accessible",
            id="Should return 'Accessible' if have internet and valid URL"
        ),

    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        url: str,
        valid_url: bool,
        internet_connection: bool,
        expected_output: str,
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page(url) == expected_output
