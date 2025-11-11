import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet, valid, expected",
    [
        (True, True, "Accessible"),        # both true => OK
        (True, False, "Not accessible"),   # only internet => fail
        (False, True, "Not accessible"),   # only url valid => fail
        (False, False, "Not accessible"),  # none => fail
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access(mock_internet, mock_valid, internet, valid, expected):
    mock_internet.return_value = internet
    mock_valid.return_value = valid

    assert can_access_google_page("https://www.google.com/") == expected
