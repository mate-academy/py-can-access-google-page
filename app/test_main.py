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
        ),
        pytest.param(
            False, False, "Not accessible",
            id="if valid url and internet connection are both False"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_for_correct_result_can_access_page(
        mocked_valid_url: mock,
        mocked_internet_connection: mock,
        valid_url: bool,
        internet_connection: bool,
        can_access: bool
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = internet_connection
    assert can_access_google_page("www.mate.com.ua") == can_access


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_internet_connection_and_valid_url_was_called(
        mocked_valid_url: mock,
        mocked_internet_connection: mock
) -> None:
    can_access_google_page("www.ua")
    mocked_internet_connection.assert_called_once()
    mocked_valid_url.assert_called_once()
