from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "url, valid_google_url, valid_internet_connection, excepted_result",
    [
        pytest.param(
            "https://google.com",
            True,
            True,
            "Accessible"
        ),
        pytest.param(
            " ",
            True,
            False,
            "Not accessible"
        ),
        pytest.param(
            "https://google.coom/",
            False,
            True,
            "Not accessible"
        ),
        pytest.param(
            "https://google.som",
            False,
            False,
            "Not accessible"
        )

    ]
)
def test_can_access_google_page(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: mock,
        url: str,
        valid_google_url: bool,
        valid_internet_connection: bool,
        excepted_result: str
) -> None:
    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_internet_connection.return_value = valid_internet_connection
    assert can_access_google_page(url=url) == excepted_result
