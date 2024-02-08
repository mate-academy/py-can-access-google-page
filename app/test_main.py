from app.main import can_access_google_page
from unittest import mock
import pytest


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url_result, connection_result, result_of_checking",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_cannot_access_if_only_valid_url(mocked_valid_url: mock,
                                         has_internet_connection: mock,
                                         url_result: bool,
                                         connection_result: bool,
                                         result_of_checking: str):
    has_internet_connection.return_value = connection_result
    mocked_valid_url.return_value = url_result
    assert can_access_google_page(" ") == result_of_checking


