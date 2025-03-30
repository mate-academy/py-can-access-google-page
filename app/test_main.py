import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    ("url", "internet_value", "url_value", "expected"),
    [
        ("https://www.google.com/", True, True, "Accessible"),
        ("https://www.youtube.com/", True, False, "Not accessible"),
        ("https://www.github.com/", False, True, "Not accessible"),
        ("https://open.spotify.com/", False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_call_url_and_internet_functions(
        mocked_internet: callable,
        mocked_url: callable,
        url: str,
        internet_value: bool,
        url_value: bool,
        expected: str,
) -> None:
    mocked_internet.return_value = internet_value
    mocked_url.return_value = url_value
    assert can_access_google_page(url) == expected
