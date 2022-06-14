import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url,is_has_internet,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page(
        mocked_valid_url,
        mocked_has_internet,
        is_valid_url,
        is_has_internet,
        result
):
    mocked_valid_url.return_value = is_valid_url
    mocked_has_internet.return_value = is_has_internet
    assert can_access_google_page("") == result
