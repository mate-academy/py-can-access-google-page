import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, google_url, expected_result",
    [
        pytest.param(
            True, True, "Accessible"
        ),
        pytest.param(
            True, False, "Not accessible"
        ),
        pytest.param(
            False, True, "Not accessible"
        ),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_can_access_google_page(
        mocked_has_internet_connection,
        mocked_valid_google_url,
        internet_connection,
        google_url,
        expected_result
):
    mocked_has_internet_connection.return_value = internet_connection
    mocked_valid_google_url.return_value = google_url
    assert can_access_google_page(google_url) == expected_result
