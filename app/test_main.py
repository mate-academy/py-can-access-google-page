import pytest

from unittest import mock

from app.main import can_access_google_page


class TestResultsOfMainFunction:
    @pytest.mark.parametrize(
        "connection_result,valid_result,expected_result",
        [
            (True, True, "Accessible"),
            (False, False, "Not accessible"),
            (False, True, "Not accessible"),
            (True, False, "Not accessible"),
        ],
    )
    def test_can_access_google_page_function(
        self, connection_result: bool, valid_result: bool, expected_result: str
    ) -> None:
        with mock.patch("app.main.has_internet_connection") as connection:
            with mock.patch("app.main.valid_google_url") as valid_google_url:
                valid_google_url.return_value = valid_result
                connection.return_value = connection_result

                assert (
                    can_access_google_page("https://www.google.com.ua")
                    == expected_result
                )

                if connection.return_value:
                    valid_google_url.assert_called_once_with(
                        "https://www.google.com.ua"
                    )
                    connection.assert_called_once()
                else:
                    connection.assert_called_once()
