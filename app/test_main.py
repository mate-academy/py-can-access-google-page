import pytest
from unittest import mock


from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_func:
        yield mocked_func


@pytest.fixture()
def mocked_has_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_func:
        yield mocked_func


def test_valid_connection_and_url_exist(mocked_valid_google_url: any,
                                        mocked_has_connection: any
                                        ) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_connection.return_value = True
    url = "http//:www.google.com/"
    assert can_access_google_page(url) == "Accessible"


def test_invalid_connection_and_valid_url_exist(mocked_valid_google_url: any,
                                                mocked_has_connection: any
                                                ) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_connection.return_value = False
    url = "http//:www.google.com/"
    assert can_access_google_page(url) == "Not accessible"


def test_valid_connection_and_invalid_url_exist(mocked_valid_google_url: any,
                                                mocked_has_connection: any
                                                ) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_connection.return_value = True
    url = "http//:www.google.com/"
    assert can_access_google_page(url) == "Not accessible"


def test_invalid_connection_and_invalid_url_exist(mocked_valid_google_url: any,
                                                  mocked_has_connection: any
                                                  ) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_connection.return_value = False
    url = "http//:www.google.com/"
    assert can_access_google_page(url) == "Not accessible"
