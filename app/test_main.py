import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid, has_connection, expected",
    [
        (True, True, "Accessible"),  # Умова: URL ок + інтернет ок
        (False, True, "Not accessible"),  # Умова: URL битий + інтернет ок
        (True, False, "Not accessible"),  # Умова: URL ок + інтернет офлайн
        (False, False, "Not accessible"),  # Умова: все погано
    ]
)
def test_can_access_google_page(is_valid: bool,
                                has_connection: bool,
                                expected: list) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url, \
            mock.patch("app.main.has_internet_connection") as mocked_conn:

        mocked_url.return_value = is_valid
        mocked_conn.return_value = has_connection

        result = can_access_google_page("https://google.com")

        assert result == expected
