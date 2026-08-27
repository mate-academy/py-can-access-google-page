import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google,has_internet,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google: object,
                                mock_has_internet: object ,
                                valid_google: bool,
                                has_internet: bool,
                                expected: str
                                ) -> None:
    mock_valid_google.return_value = valid_google
    mock_has_internet.return_value = has_internet
    assert can_access_google_page("https://www.google.com/") == expected
