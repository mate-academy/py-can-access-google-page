import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_internet,mock_url,expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet_con: mock,
                                mock_valid_url: mock,
                                mock_url: mock,
                                mock_internet: mock,
                                expected: str) -> None:
    mock_internet_con.return_value = mock_internet
    mock_valid_url.return_value = mock_url

    assert can_access_google_page("http/google.com") == expected
