import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture
def mocked_connect() -> mock:
    with mock.patch("app.main.has_internet_connection") as connect:
        yield connect


@pytest.fixture
def mocked_valid() -> mock:
    with mock.patch("app.main.valid_google_url") as valid:
        yield valid


@pytest.mark.parametrize(
    "url,result,connect_val,valid_val",
    [
        ("first url", "Accessible", True, True),
        ("second url", "Not accessible", True, False),
        ("third url", "Not accessible", False, True),
        ("four's url", "Not accessible", False, False)
    ],
    ids=[
        "should return Accessible when connect and valid true",
        "should return Not accessible when connect,valid == true, false",
        "should return Not accessible when connect,valid == false, true",
        "should return Not accessible when connect,valid == false, false"
    ]
)
def test_return_accessible_only_if_connect_and_valid(
        mocked_connect: mock,
        mocked_valid: mock,
        url: str,
        result: str,
        connect_val: bool,
        valid_val: bool
) -> None:
    mocked_valid.return_value = valid_val
    mocked_connect.return_value = connect_val
    assert can_access_google_page(url) == result
