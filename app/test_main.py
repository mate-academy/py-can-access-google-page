from unittest import mock
import pytest
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "true_url,internet_connection,expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="if both functions works, "
               "should return 'Accessible'",
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="both functions are not accessible",
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="url is not valid",
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="no internet connection",
        ),
    ],
)
def test_can_access_google_page(mock_valid_url,
                                mock_internet_connection,
                                true_url,
                                internet_connection,
                                expected):
    mock_valid_url.return_value = true_url
    mock_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://google.com") == expected
