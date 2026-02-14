import pytest
from app.main import can_access_google_page
from pytest_mock import MockerFixture


@pytest.mark.parametrize(
    "valid_url,has_connection,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_valid_url_and_connection_exists(mocker: MockerFixture,
                                         valid_url: bool,
                                         has_connection: bool,
                                         expected: str) -> None:
    mocker.patch("app.main.valid_google_url",
                 return_value=valid_url)
    mocker.patch("app.main.has_internet_connection",
                 return_value=has_connection)
    assert can_access_google_page("https://www.google.com/") == expected
