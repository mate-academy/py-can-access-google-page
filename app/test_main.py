from unittest import mock
from pytest import mark, param

from app.main import can_access_google_page


@mark.parametrize("url_status,connection_status,access_status",
                  [
                      param(True, True, "Accessible",
                            id="url and connection ok"),
                      param(False, True, "Not accessible",
                            id="bad url"),
                      param(True, False, "Not accessible",
                            id="bad connection"),
                      param(False, False, "Not accessible",
                            id="bad url and connection"),
                  ])
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_validate_access(mocked_url: mock.Mock,
                                mocked_connection: mock.Mock,
                                url_status: bool, connection_status: bool,
                                access_status: str) -> None:
    mocked_url.return_value = url_status
    mocked_connection.return_value = connection_status

    assert can_access_google_page("https://google.com") == access_status
