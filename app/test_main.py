import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_internet,expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="test connection and url are true"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test only connection is false"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test only url is false"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_valid_google_url,
                                mocked_has_internet_connection,
                                valid_url,
                                has_internet,
                                expected):
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = has_internet
    assert can_access_google_page("https://www.google.com/") == expected
