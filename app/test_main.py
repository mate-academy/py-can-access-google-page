import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_connection,expect_value",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_google_url: mock,
                                mock_has_internet_connection: mock,
                                valid_url: bool,
                                has_connection: bool,
                                expect_value: str) -> None:
    sites = ["https://www.google.com",
             "https://mate.academy/",
             "https://www.youtube.com/"]
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_connection
    for site in sites:
        assert can_access_google_page(site) == expect_value
