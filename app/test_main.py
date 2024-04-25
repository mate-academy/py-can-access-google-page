import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture
def mock_test_valid_google_url() -> bool:
    with mock.patch("app.main.valid_google_url") as mock_google_url:
        yield mock_google_url


@pytest.fixture
def mock_test_has_internet_connection() -> bool:
    with mock.patch(
        "app.main.has_internet_connection"
    ) as mock_has_internet_connection:
        yield mock_has_internet_connection


@pytest.mark.parametrize(
    "url_address",
    [("https://www.google.com/"), ("https://ja.wikipedia.org/wiki/"), ("abc")],
)
def test_dependant_functions(
    url_address: str,
    mock_test_has_internet_connection: None,
    mock_test_valid_google_url: None
) -> None:

    can_access_google_page(url=url_address)
    mock_test_has_internet_connection.assert_called_once()
    mock_test_valid_google_url.assert_called_once_with(url_address)


@pytest.mark.parametrize(
    "url_address,return_of_connection,result,return_url",
    [
        ("https://www.google.com/", True, "Accessible", True),
        ("https://ja.wikipedia.org/wiki/", True, "Not accessible", False),
        ("abc1", False, "Not accessible", False),
        ("abc", False, "Not accessible", True),
    ],
)
def test_return_can_access_google_page(
    url_address: str,
    return_of_connection: bool,
    result: str,
    mock_test_has_internet_connection: None,
    mock_test_valid_google_url: None,
    return_url: bool,
) -> None:
    mock_test_has_internet_connection.return_value = return_of_connection
    mock_test_valid_google_url.return_value = return_url
    can_access_google_page(url=url_address)
    assert (
        can_access_google_page(url=url_address) == result
    ), f"Function should return {result}"
