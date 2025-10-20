from unittest import mock
import pytest
from typing import Any
from app.main import can_access_google_page


@pytest.fixture()
def mocked_function1() -> Any:
    with mock.patch("app.main.has_internet_connection") as mocked1:
        yield mocked1


@pytest.fixture()
def mocked_function2() -> Any:
    with mock.patch("app.main.valid_google_url") as mocked2:
        yield mocked2


def test_valid_url_only(mocked_function1: Any, mocked_function2: Any) -> None:
    mocked_function1.return_value = False
    mocked_function2.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


def test_internet_only(mocked_function1: Any, mocked_function2: Any) -> None:
    mocked_function1.return_value = True
    mocked_function2.return_value = False
    result = can_access_google_page("bad link")
    assert result == "Not accessible"

def test_accessible(mocked_function1: Any, mocked_function2: Any) -> None:
    mocked_function1.return_value = True
    mocked_function2.return_value = True
    result = can_access_google_page("good link")
    assert result == "Accessible"