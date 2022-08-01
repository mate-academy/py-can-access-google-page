import pytest
from unittest import mock

from app import main


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as valid_url:
        yield valid_url


@pytest.fixture()
def mocked_internet_connection():
    with mock.patch("app.main.has_internet_connection") as connection:
        yield connection


@pytest.mark.parametrize("url_response,has_connection,result",
                         [
                             pytest.param(True, True, "Accessible",
                                          id="Test with access and connection"),
                             pytest.param(True, False, "Not accessible",
                                          id="Test without internet connection"),
                             pytest.param(False, True, "Not accessible",
                                          id="Test without access"),
                             pytest.param(False, False, "Not accessible",
                                          id="Test without access and connection")
                         ]
                         )
def test_can_access_google_pege(mocked_valid_url,
                                mocked_internet_connection,
                                url_response,
                                has_connection,
                                result):
    mocked_valid_url.return_value = url_response
    mocked_internet_connection.return_value = has_connection
    assert main.can_access_google_page("") == result

