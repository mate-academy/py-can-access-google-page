from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture
def mock_has_con() -> bool:
    with mock.patch("app.main.has_internet_connection") as mock_has_con:
        yield mock_has_con


@pytest.fixture
def mock_valid_url() -> bool:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.mark.parametrize(
    "valid_url,has_con,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
)
def test_valid_url_and_connection_exists(
        mock_has_con: callable,
        mock_valid_url: callable,
        valid_url: bool,
        has_con: bool,
        result: str) -> None:
    mock_has_con.return_value = has_con
    mock_valid_url.return_value = valid_url
    assert can_access_google_page("") == result
