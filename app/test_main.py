from app.main import can_access_google_page
from unittest import mock
import pytest
from unittest.mock import MagicMock


@pytest.mark.parametrize("url, result", [
    pytest.param(
        "https://www.google.com/",
        "Accessible",
        id="return with valid url and connection"
    ),
    pytest.param(
        "https://t.ly/ThI2P",
        "Not accessible",
        id="return with not valid url"
    )
])
def test_can_access_google_page_return(url: str, result: str) -> None:
    assert can_access_google_page(url) == result


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_ext_funcs_call(
        mocked_has_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock
) -> None:

    url = "https://www.google.com/"
    can_access_google_page(url)

    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with(url)
