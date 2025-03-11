from unittest import mock
import pytest
from .main import can_access_google_page


@pytest.fixture
def mocked_valid_url() -> None:
    with mock.patch("main.valid_google_url") as mock_test_valid:
        yield mock_test_valid


@pytest.fixture
def mocked_has_connection() -> None:
    with (mock.patch("main.has_internet_connection") as
          mock_test_has_connection):
        yield mock_test_has_connection


def test_can_access_valid_url_and_has_connection(mock_valid: mock,
                                                 mock_connection: mock
                                                 ) -> bool:
    mock_valid.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("http://www.google.com") == "Accessible"


def test_can_access_google_page_invalid_url(mock_valid: mock,
                                            mock_connection: mock
                                            ) -> bool:
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = True
    assert can_access_google_page("http://www.google.com") == "Not accessible"


def test_can_access_google_page_has_no_connection(mock_valid: mock,
                                                  mock_connection: mock
                                                  ) -> bool:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"


def test_can_access_page_no_connection_invalid_url(mock_valid: mock,
                                                   mock_connection: mock
                                                   ) -> bool:
    mocked_valid_url.return_value = False
    mocked_has_connection.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"
