from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, can_access",
    [
        pytest.param(
            True, False, "Not accessible",
            id="if valid google url is failing"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="if internet connection is failing"
        ),
        pytest.param(
            True, True, "Accessible",
            id="if valid url and internet connection are both True"
        )
    ]
)
def test_for_some(
        valid_url: bool,
        internet_connection: bool,
        can_access: bool
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        with mock.patch(
                "app.main.has_internet_connection"
        ) as mocked_internet_connection:
            mocked_valid_url.return_value = valid_url
            mocked_internet_connection.return_value = internet_connection
            assert can_access_google_page("www.mate.com.ua") == can_access


def test_valid_url_was_called() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        can_access_google_page("www.com")
        mocked_valid_url.assert_called_once()


def test_internet_connection_and_valid_url_was_called() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        with mock.patch(
                "app.main.has_internet_connection"
        ) as mocked_internet_connection:
            can_access_google_page("www.ua")
            mocked_internet_connection.assert_called_once()
            mocked_valid_url.assert_called_once()
