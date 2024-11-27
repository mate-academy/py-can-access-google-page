from unittest import mock
from typing import Callable
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessible_url_with_valid_conditions(
        mocked_url: Callable,
        mocked_internet_connection: Callable) -> None:
    assert can_access_google_page("https://mate.academy/learn/"
                                  "python-core/python-core-"
                                  "testing-in-details?"
                                  "learnItemsFilter="
                                  "All&section=video"
                                  "&theoryId=3664&videoId"
                                  "=2193&testTaskSlug="
                                  "py_can_access_google_page") == "Accessible"


@mock.patch("app.main.valid_google_url")
def test_call_valid_google_url(mocked_url: Callable) -> None:
    can_access_google_page("https://page")
    mocked_url.assert_called_once_with("https://page")


@mock.patch("app.main.has_internet_connection")
def test_call_has_internet_connection(mocked_internet_connection: Callable) \
        -> None:
    can_access_google_page("https://www.google.com/search?"
                           "q=url&oq=url&gs_lcrp=EgZjaHJvbWUyC"
                           "QgAEEUYORiABDIHCAEQABiABDIHCAIQABi"
                           "ABDIHCAMQABiABDIGCAQQRRg8MgYIBRBFG"
                           "DwyBggGEEUYPDIGCAcQRRg80gEINTE0Nmo"
                           "wajeoAgewAgE&sourceid=chrome&ie=UTF-8")
    mocked_internet_connection.assert_called_once_with()
