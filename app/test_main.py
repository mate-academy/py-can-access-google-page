from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_validity,internet_connection,expected_result",
    [
        pytest.param(
            True, True, "Accessible",
            id="should return 'Accessible' if url is valid and internet connection available"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="should return 'Not accessible' if no internet connection"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="should return 'Not accessible' if url not valid"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="should return not accessible if both params are False"
        )
    ]
)
def test_internet_connection_and_url_validity(url_validity: bool,
                                              internet_connection: bool,
                                              expected_result: str) -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mock_has_internet_connection,
        mock.patch("app.main.valid_google_url") as mock_valid_google_url
    ):
        mock_valid_google_url.return_value = url_validity
        mock_has_internet_connection.return_value = internet_connection
        assert can_access_google_page("https://music.youtube.com/") == expected_result
