from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture
def mock_has_con(result: bool) -> bool:
    with mock.patch("app.main.has_internet_connection") as mock_has_con:
        return result


@pytest.fixture
def mock_valid_url(result: bool) -> bool:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        return result


@pytest.mark.parametrize(
    "valid_url,has_con,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
)
def test_can_access_google_page(
        mock_has_con,
        mock_valid_url,
        valid_url: bool,
        has_con: bool,
        result: str):
    mock_has_con.return_value = has_con
    mock_valid_url.return_value = valid_url
    assert can_access_google_page("") == result
