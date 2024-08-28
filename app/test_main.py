import pytest

from unittest import mock

from app.main import can_access_google_page


test_url = "url"


@pytest.fixture(scope="module")
def mock_valid_url() -> bool:
    with (mock.patch("app.main.valid_google_url")
          as mock_url):
        yield mock_url


@pytest.fixture(scope="module")
def mock_internet_connect() -> bool:
    with (mock.patch("app.main.has_internet_connection")
          as mock_connect):
        yield mock_connect


@pytest.mark.parametrize(
    "google_url, internet_connection, url, permission",
    [
        pytest.param(
            True, True, "url", "Accessible",
            id="accessible"
        ),
        pytest.param(
            True, False, "url", "Not accessible",
            id="not accessible"
        ),
        pytest.param(
            False, True, "url", "Not accessible",
            id="not accessible"
        ),
        pytest.param(
            False, False, "url", "Not accessible",
            id="not accessible"
        )
    ]
)
def test_can_access_google_page(
        mock_valid_url: bool,
        mock_internet_connect: bool,
        google_url: bool,
        internet_connection: bool,
        url: str,
        permission: str
) -> None:
    mock_valid_url.return_value = google_url
    mock_internet_connect.return_value = internet_connection

    assert can_access_google_page(test_url) == permission
