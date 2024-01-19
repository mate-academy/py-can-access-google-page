import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,url_is_valid,internet_is_connected,expected_output",
    [
        ("https://kaz-tili.kz/index.htm", True, True, "Accessible"),
        ("https://kaz-tili.kz/index.htm", False, True, "Not accessible"),
        ("https://kaz-tili.kz/index.htm", True, False, "Not accessible"),
        ("https://kaz-tili.kz/index.htm", False, False, "Not accessible")
    ],
    ids=(
        "test can access google page",
        "has invalid google url",
        "does not have an access to the Internet",
        "url is invalid and no connection to the Internet"
    )
)
def test_access_google_page(
        url,
        url_is_valid,
        internet_is_connected,
        expected_output
):
    with (mock.patch("app.main.valid_google_url") as mock_valid_url,
          mock.patch("app.main.has_internet_connection") as mock_interned_connection):
        mock_valid_url.return_value = url_is_valid
        mock_interned_connection.return_value = internet_is_connected
        assert can_access_google_page(url) == expected_output
