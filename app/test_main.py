from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection,is_valid_url,expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Page is accessible"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="No internet connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="No internet connection and page is not accessible",
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Page is not accessible",
        )
    ]
)
def test_should_return_correct_data(
        has_connection: bool,
        is_valid_url: bool,
        expected_result: str
) -> None:
    testing_url = "https://www.youtube.com/"
    with (mock.patch("app.main.has_internet_connection") as mocked_time,
          mock.patch("app.main.valid_google_url") as mocked_url_check):
        mocked_url_check.return_value = is_valid_url
        mocked_time.return_value = has_connection
        assert can_access_google_page(testing_url) == expected_result
