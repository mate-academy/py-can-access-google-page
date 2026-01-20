from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "link, valid_url, internet_connection, expected",  #
    [
        pytest.param(
            "https://translate.google.com/?hl=ru",
            False,
            True,
            "Not accessible",
            id="test_cannot_access_if_only_connection_true"
        ),
        pytest.param(
            "https://translate.google.com/?hl=ru",
            True,
            False,
            "Not accessible",
            id="test_cannot_access_if_connection_or_valid_url_is_true"

        ),
        pytest.param(
            "https://translate.google.com/?hl=ru",
            True,
            True,
            "Accessible",
            id="test_access_if_connection_and_valid_url_true"

        )
    ])
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mocked_valid_url,
                                mocked_connection,
                                link,
                                valid_url,
                                internet_connection,
                                expected):
    mocked_valid_url.return_value = valid_url
    mocked_connection.return_value = internet_connection
    assert can_access_google_page(link) == expected
