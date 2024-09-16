from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_check,connection_check,result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        url_check: bool, connection_check: bool, result: str
) -> None:
    with (
        mock.patch(
            "app.main.valid_google_url"
        ) as mock_valid_google_url,
        mock.patch(
            "app.main.has_internet_connection"
        ) as mock_has_internet_connection
    ):
        mock_valid_google_url.return_value = url_check
        mock_has_internet_connection.return_value = connection_check

        assert can_access_google_page("https://www.youtube.com") == result

        mock_has_internet_connection.assert_called_once()
        if connection_check:
            mock_valid_google_url.assert_called_once_with(
                "https://www.youtube.com"
            )
