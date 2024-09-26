from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_has_internet:
        yield mock_has_internet


def test_function_correct_work(mocked_valid_url,
                               mocked_has_internet_connection):
    mocked_has_internet_connection.return_value = True
    mocked_valid_url.return_value = True

    assert can_access_google_page("") == "Accessible", \
        "Function must return 'Accessible' when " \
        "internet connection and google url return True"


def test_if_only_internet_connection_true(mocked_valid_url,
                                          mocked_has_internet_connection):
    mocked_valid_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("") == "Not accessible", \
        "Function must return 'Not accessible' " \
        "if internet connection return False"


def test_if_only_valid_url_true(mocked_valid_url,
                                mocked_has_internet_connection):
    mocked_valid_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("") == "Not accessible", \
        "Function must return 'Not accessible' " \
        "if google url return False"


def test_if_all_function_return_false(mocked_valid_url,
                                      mocked_has_internet_connection):
    mocked_valid_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("") == "Not accessible", \
        "Function must return 'Not accessible' if google url " \
        "and internet connection return False"
