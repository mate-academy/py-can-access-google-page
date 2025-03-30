import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, access, check_1, check_2",
    [
        ("https://www.google.com/?&bih=707&biw=744&hl=uk",
            "Accessible",
            True,
            True),
        ("https://forum/index.php/sjdhvfjsgdvfjsd",
            "Not accessible",
            False,
            True),
        ("https://www.google.com/?&bih=707&biw=744&hl=uk",
            "Not accessible",
            True,
            False),
        ("https://forum/index.php/sjdhvfjsgdvfjsd",
            "Not accessible",
            False,
            False)
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_internet_connection,
        mocked_valid_google_url,
        url,
        access,
        check_1,
        check_2):
    mocked_internet_connection.return_value = check_1
    mocked_valid_google_url.return_value = check_2
    assert can_access_google_page(url) == access
