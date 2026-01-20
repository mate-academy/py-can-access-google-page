import pytest
from unittest import mock
from app.main import can_access_google_page

CONNECTION_URL = "http://www.google.com"


@pytest.mark.parametrize(
    "has_internet, is_valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(has_internet: bool,
                                is_valid_url: bool,
                                expected_result: str) -> None:
    with mock.patch("app.main.has_internet_connection") as mock_has_internet:
        with mock.patch("app.main.valid_google_url") as mock_is_valid_url:
            mock_has_internet.return_value = has_internet

            if has_internet:
                mock_is_valid_url.return_value = is_valid_url
            else:
                mock_is_valid_url.return_value = False

            result = can_access_google_page(CONNECTION_URL)
            assert result == expected_result

            if has_internet:
                assert mock_is_valid_url.called
            else:
                assert not mock_is_valid_url.called
