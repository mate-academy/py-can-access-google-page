import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture
def mocked_valid_url() -> mock.Mock:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture
def mocked_internet_connection() -> mock.Mock:
    with mock.patch("app.main.has_internet_connection") as mocked_url:
        yield mocked_url


@pytest.mark.parametrize(
    "url,validation,connection,expected_result",
    [
        pytest.param(
            "mate.academy", True, True, "Accessible"
        ),
        pytest.param(
            "mate.academy", True, False, "Not accessible"
        ),
        pytest.param(
            "mate.academy", False, True, "Not accessible"
        ),
        pytest.param(
            "mate.academy", False, False, "Not accessible"
        ),
    ]
)
def test_can_access_google_page(
        url: str,
        validation: bool,
        connection: bool,
        expected_result: str,
        mocked_valid_url: mock.Mock,
        mocked_internet_connection: mock.Mock
) -> None:
    mocked_valid_url.return_value = validation
    mocked_internet_connection.return_value = connection
    assert can_access_google_page(url) == expected_result
