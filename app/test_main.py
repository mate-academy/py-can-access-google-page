import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "has_internet,is_valid_url,expected",
    [
        pytest.param(True, True, "Accessible",
                     id="valid url with connection"),
        pytest.param(True, False, "Not accessible",
                     id="invalid url with connection"),
        pytest.param(False, True, "Not accessible",
                     id="valid url without connection"),
        pytest.param(False, False, "Not accessible",
                     id="invalid_url_without_connection"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_valid_url: mock.Mock,
        mocked_has_internet: mock.Mock,
        has_internet: bool,
        is_valid_url: bool,
        expected: str,
) -> None:
    mocked_has_internet.return_value = has_internet
    mocked_valid_url.return_value = is_valid_url

    assert can_access_google_page("google.com") == expected
