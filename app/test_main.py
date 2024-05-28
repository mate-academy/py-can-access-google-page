from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,expected_result,has_internet,valid_url",
    [
        pytest.param(
            "https://www.google.com",
            "Not accessible",
            False,
            True,
            id="Not accessible without internet"
        ),
        pytest.param(
            "https://www.google.com",
            "Not accessible",
            False,
            False,
            id="Not accessible when invalid url and no internet"
        ),
        pytest.param(
            "https://www.google.com",
            "Not accessible",
            True,
            False,
            id="Not accessible when invalid url"
        ),
        pytest.param(
            "https://www.google.com",
            "Accessible",
            True,
            True,
            id="Accessible when has internet and valid url"
        ),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_internet_connection: callable,
        mocked_valid_url: callable,
        url: str,
        expected_result: str,
        has_internet: bool,
        valid_url: bool
) -> None:
    mocked_internet_connection.return_value = has_internet
    mocked_valid_url.return_value = valid_url
    assert can_access_google_page(url) == expected_result
