import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, is_internet_connect, result_load_page",
    [
        pytest.param(
            True, False, "Not accessible",
            id="Not connect internet"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="Google url is not valid"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Not valid url and not connect internet"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="Google page - Accessible"
        ),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_page_access(
        mock_has_internet: mock.Mock,
        mock_valid_url: mock.Mock,
        is_valid_url: bool,
        is_internet_connect: bool,
        result_load_page: str
) -> None:
    mock_has_internet.return_value = is_internet_connect
    mock_valid_url.return_value = is_valid_url

    assert can_access_google_page("url") == result_load_page
