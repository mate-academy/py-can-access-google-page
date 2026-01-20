import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_ural, has_internet, result",
    [(True, True, "Accessible",),
     (False, True, "Not accessible"),
     (True, False, "Not accessible"),
     (False, False, "Not accessible")]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_check_can_access_google_page(
        mocked_url: object,
        mocked_internet: object,
        valid_ural: bool,
        has_internet: bool,
        result: str) -> None:
    mocked_url.return_value = valid_ural
    mocked_internet.return_value = has_internet
    assert can_access_google_page("google.com") == result
