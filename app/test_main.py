from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.fixture()
def mock_requests() -> None:
    with mock.patch("app.main.valid_google_url") as mock_test_requests:
        yield mock_test_requests


@pytest.fixture()
def mock_datetime() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_test_datetime:
        yield mock_test_datetime


@pytest.mark.parametrize(
    "valid_url,internet_connection,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=["test1: True,True must have result 'Accessible'",
         "test2: True,False must have result 'Not accessible'",
         "test3: False,True must have result 'Not accessible'",
         "test4: False,False must have result 'Not accessible'", ]
)
def test_url_valid_and_internet_connection(mock_requests: mock.Mock,
                                           mock_datetime: mock.Mock,
                                           valid_url: bool,
                                           internet_connection: bool,
                                           result: str) -> None:
    mock_requests.return_value = valid_url
    mock_datetime.return_value = internet_connection
    assert can_access_google_page("https://google.com/") == result
