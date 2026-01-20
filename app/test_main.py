import pytest
from unittest import mock


import app.main


@pytest.mark.parametrize(
    "url_is_valid,connection_is_ok,expected_result",
    [
        pytest.param(True, True, "Accessible",
                     id="url and connection are ok"),

        pytest.param(False, True, "Not accessible",
                     id="url is not valid, connection is ok"),

        pytest.param(True, False, "Not accessible",
                     id="url is ok, but no connection"),

        pytest.param(False, False, "Not accessible",
                     id="both url and connection are not ok"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_valid_google_url: mock.MagicMock,
                                mocked_has_internet_connection: mock.MagicMock,
                                url_is_valid: bool,
                                connection_is_ok: bool,
                                expected_result: str
                                ) -> None:

    mocked_valid_google_url.return_value = url_is_valid
    mocked_has_internet_connection.return_value = connection_is_ok
    assert expected_result == app.main.can_access_google_page("www.google.com")
