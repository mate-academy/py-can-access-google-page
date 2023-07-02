import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet, valid, result",
    [
        pytest.param(True, True, "Accessible",
                     id="has_internet_connection == True,"
                        " valid_google_url == True,"
                        " Accessible"),

        pytest.param(True, False, "Not accessible",
                     id="has_internet_connection == True,"
                        " valid_google_url == False,"
                        " Not accessible"),
        pytest.param(False, True, "Not accessible",
                     id="has_internet_connection == False,"
                        " valid_google_url == True,"
                        " Not accessible"),
        pytest.param(False, False, "Not accessible",
                     id="has_internet_connection == False,"
                        " valid_google_url == False,"
                        " Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_has_internet_connection: mock,
        mocked_valid_google_url: mock,
        internet: bool,
        valid: bool,
        result: str
) -> None:
    mocked_has_internet_connection.return_value = internet
    mocked_valid_google_url.return_value = valid
    assert can_access_google_page("url") == result
