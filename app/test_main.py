from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, is_valid_url, outcome",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_if_one_can_access_google_page(
        internet_connection: bool,
        is_valid_url: bool,
        outcome: str
) -> None:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mock_has_internet_connection,\
        mock.patch(
            "app.main.valid_google_url"
    ) as mock_valid_url:
        mock_has_internet_connection.return_value = internet_connection
        mock_valid_url.return_value = is_valid_url
        assert can_access_google_page("") == outcome
