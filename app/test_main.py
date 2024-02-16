import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, has_internet, result",
    [
        pytest.param(
            "https://www.google.com/",
            True, True, "Accessible",
            id="Valid url and has connection."
        ),

        pytest.param(
            "http://lottery.net/",
            False, True, "Not accessible",
            id="Invalid url and has connection."
        ),

        pytest.param(
            "https://www.google.com/",
            True, False, "Not accessible",
            id="Valid url and no connection."
        ),

        pytest.param(
            "http://moonobank.ua/",
            False, False, "Not accessible",
            id="Invalid url and no connection."
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_url: mock.MagicMock,
        mocked_internet_connection: mock.MagicMock,
        url: str, valid_url: bool, has_internet: bool,
        result: str
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = has_internet

    assert can_access_google_page(url) == result
