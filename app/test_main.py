from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_internet, result",
    [
        pytest.param(
            True, True, "Accessible",
            id="Valid url with internet connection."
        ),
        pytest.param(
            False, True, "Not accessible",
            id="Invalid url with internet connection."
        ),
        pytest.param(
            True, False, "Not accessible",
            id="Valid url without internet connection."
        ),
        pytest.param(
            False, False, "Not accessible",
            id="Invalid url without internet connection."
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_url: mock.MagicMock,
        mocked_internet_connection: mock.MagicMock,
        valid_url: bool, has_internet: bool, result: str
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = has_internet

    assert can_access_google_page("https://www.google.com") == result
