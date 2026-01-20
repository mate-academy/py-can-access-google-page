from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection,message",
    [
        pytest.param(True, True, "Accessible",
                     id="should return accessible_if_all_true"),
        pytest.param(False, False, "Not accessible",
                     id="should return not accessible_if_all_false"),
        pytest.param(True, False, "Not accessible",
                     id="should return not accessible_if_any_false"),
        pytest.param(False, True, "Not accessible",
                     id="should return not accessible_if_any_false")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: mock,
        valid_google_url: bool,
        has_internet_connection: bool,
        message: str
) -> None:
    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("https://google.com") == message
