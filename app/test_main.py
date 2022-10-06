import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture
def mocked_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.fixture
def mocked_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.mark.parametrize(
    "valid_url, net_connection, expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="all param valid"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="wrong time"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="wrong url"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="all param wrong"
        )
    ]
)
def test_access_google_page(mocked_valid_url: bool,
                            mocked_internet_connection: bool,
                            valid_url: bool,
                            net_connection: bool,
                            expected: str) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = net_connection
    assert can_access_google_page(valid_url) == expected
