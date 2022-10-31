import pytest

from app.main import can_access_google_page

from unittest import mock


@pytest.fixture()
def mocked_valid_google_url():
    with mock.patch("app.main.valid_google_url") as google_url:
        yield google_url


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as internet_connect:
        yield internet_connect


@pytest.mark.parametrize("url_value,connection_value,result",
                         [
                             pytest.param(True, True, "Accessible",
                                          id="Test when Url "
                                             "and Connection is True"),
                             pytest.param(True, False, "Not accessible",
                                          id="Test when Url is True "
                                             "and Connection is False"),
                             pytest.param(False, True, "Not accessible",
                                          id="Test when Url is False "
                                             "and Connection is True"),
                             pytest.param(False, False, "Not accessible",
                                          id="Test when Url and "
                                             "Connection is False")
                         ]
                         )
def test_can_access_google_pege(mocked_valid_google_url,
                                mocked_has_internet_connection,
                                url_value,
                                connection_value,
                                result):
    mocked_valid_google_url.return_value = url_value
    mocked_has_internet_connection.return_value = connection_value
    assert can_access_google_page("") == result
# the end