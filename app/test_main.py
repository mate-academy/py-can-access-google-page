from unittest import mock
import pytest

import app.main


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_url, has_internet, expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="test valid url and has internet connection"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="test should not access with no internet connection"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="test should not access with invalid url"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="test invalid url and no internet connection"
        )
    ]
)
def test_can_check_accessibility_correctly(
    mocked_valid_url: mock.MagicMock,
    mocked_has_internet: mock.MagicMock,
    valid_url: bool,
    has_internet: bool,
    expected: str
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_has_internet.return_value = has_internet
    assert app.main.can_access_google_page("") == expected
