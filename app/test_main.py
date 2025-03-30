import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_func, valid_url_func, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
    ],
    ids=[
        "test can access google page",
        "test cannot access to internet connection",
        "test cannot access to internet and doesnt have internet connection",
        "test doesnt have internet connection",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: callable,
        mock_has_internet_connection: callable,
        internet_func: bool,
        valid_url_func: bool,
        result: str
) -> None:
    mock_has_internet_connection.return_value = internet_func
    mock_valid_google_url.return_value = valid_url_func
    assert can_access_google_page("https://www.google.com") == result
