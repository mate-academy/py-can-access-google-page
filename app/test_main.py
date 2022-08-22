from unittest import mock

import app.main as main


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_url, mocked_connection):
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert main.can_access_google_page("") == "Accessible",\
        "Can access. Should return True"
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert main.can_access_google_page("") == "Not accessible",\
        "Not access url is not valid. Should return False"
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert main.can_access_google_page("") == "Not accessible", \
        "Not access time out of range. Should return False"
    mocked_url.return_value = False
    mocked_connection.return_value = False
    assert main.can_access_google_page("") == "Not accessible",\
        "Not access url is not valid and time out of range. " \
        "Should return False"
