from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,valid_google_url,has_internet_connection,expected_result",
    [
        pytest.param(
            "https://translate.google.com/?hl=uk",
            True,
            True,
            "Accessible",
            id="if valid url and connection exists"
        ),
        pytest.param(
            "translate.google.com/?hl=uk",
            False,
            True,
            "Not accessible",
            id="cannot access if only connection"
        ),
        pytest.param(
            "https://translate.google.com/?hl=uk",
            True,
            False,
            "Not accessible",
            id="cannot access if only valid url"
        ),
        pytest.param(
            "https://translate.google.com/?hl=uk",
            False,
            False,
            "Not accessible",
            id="cannot access if invalid url and no connection"
        ),
    ]
)
def test_accessing_page_correctly(
        url: str,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected_result: str
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_google_url:
        with mock.patch("app.main.has_internet_connection") as mocked_has_internet_connection:
            mocked_valid_google_url.return_value = valid_google_url
            mocked_has_internet_connection.return_value = has_internet_connection
            assert (can_access_google_page(url)
                    == expected_result)
