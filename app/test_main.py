import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, actual",
    [
        pytest.param(
            True, True, "Accessible", id="test_both_valid_url_and_internet"
        ),
        pytest.param(
            True, False, "Not accessible", id="test_valid_url_but_no_internet"
        ),
        pytest.param(
            False, True, "Not accessible", id="test_internet_but_invalid_url"
        ),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_to_url(
        mocked_valid_google_url: None,
        mocked_has_internet_connection: None,
        valid_url: bool,
        internet_connection: bool,
        actual: str
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = internet_connection
    if mocked_valid_google_url.return_value\
            and mocked_has_internet_connection.return_value:
        assert can_access_google_page("www.google.com") == actual
    else:
        assert can_access_google_page("www.") == actual
