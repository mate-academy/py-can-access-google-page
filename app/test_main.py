from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_func_valid() -> None:
    with mock.patch("app.main.valid_google_url") as mock_func_valid:
        yield mock_func_valid


@pytest.fixture()
def mock_func_has_internet_connect() -> None:
    with mock.patch("app.main.has_internet_connection") \
            as mock_func_has_internet_connect:
        yield mock_func_has_internet_connect


def test_connection_access(
        mock_func_valid: mock,
        mock_func_has_internet_connect: mock
) -> None:
    mock_func_valid.return_value = True
    mock_func_has_internet_connect.return_value = True
    assert can_access_google_page("https://mate.academy/") == "Accessible"


def test_connection_not_access(
        mock_func_valid: mock,
        mock_func_has_internet_connect: mock
) -> None:
    mock_func_valid.return_value = True
    mock_func_has_internet_connect.return_value = False
    assert can_access_google_page("https://mate.academy/") == "Not accessible"


def test_not_valid_connect(
        mock_func_valid: mock,
        mock_func_has_internet_connect: mock
) -> None:
    mock_func_valid.return_value = False
    mock_func_has_internet_connect.return_value = True
    assert can_access_google_page("https://mate.academy/") == "Not accessible"


def test_all_not_connect(
        mock_func_valid: mock,
        mock_func_has_internet_connect: mock
) -> None:
    mock_func_valid.return_value = False
    mock_func_has_internet_connect.return_value = False
    assert can_access_google_page("https://mate.academy/") == "Not accessible"
