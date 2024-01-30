import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_has_valid_url() -> mock:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mock_test_valid_url:
        yield mock_test_valid_url


@pytest.fixture()
def mocked_has_internet() -> mock:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as has_internet_connection:
        yield has_internet_connection


@pytest.mark.parametrize(
    "url, connection, result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ], ids=[
        "if connection not exists should return 'Not accessible'",
        "if in valid url and connection exists should return 'Not accessible'",
        "if valid url and connection exists should return 'Accessible'"
    ]
)
def test_return_correct_message(
        url: bool, connection: bool, result: str,
        mocked_has_valid_url: mock, mocked_has_internet: mock
) -> None:
    mocked_has_valid_url.return_value = url
    mocked_has_internet.return_value = connection
    assert can_access_google_page("some.url") == result
