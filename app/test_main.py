from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected",
    [
        pytest.param(True, True, "Accessible",
                     id="Return 'Accessible' if valid_google_url "
                        "and has_internet_connection return True"),
        pytest.param(True, False, "Not accessible",
                     id="Return 'Not accessible' if valid_google_url is True "
                        "but has_internet_connection return False"),
        pytest.param(False, True, "Not accessible",
                     id="Return 'Not accessible' if valid_google_url is False "
                        "but has_internet_connection return True"),
        pytest.param(False, False, "Not accessible",
                     id="Return 'Not accessible' if valid_google_url is False "
                        "and also has_internet_connection return False")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mocked_valid_url: mock.MagicMock,
                                mocked_connection: mock.MagicMock,
                                valid_url: bool,
                                has_connection: bool,
                                expected: str) -> None:

    mocked_valid_url.return_value = valid_url
    mocked_connection.return_value = has_connection
    assert can_access_google_page("www.google.com") == expected
