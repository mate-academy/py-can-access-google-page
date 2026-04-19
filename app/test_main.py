import pytest
from pytest_mock import MockerFixture

from app.main import can_access_google_page


class TestAccessGooglePage:
    url = "https://test-page/"

    @pytest.mark.parametrize(
        "valid_url, has_connection, expected", [
            (True, True, "Accessible"),
            (False, False, "Not accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible")
        ], ids=[
            "Result if valid url and has connection",
            "Result if not valid url and hasn't connection",
            "Result if valid url and hasn't connection",
            "Result if not valid url and has connection"
        ])
    def test_can_access_google_page(
            self,
            mocker: MockerFixture,
            valid_url: bool,
            has_connection: bool,
            expected: str
    ) -> None:

        mock_valid_url = mocker.patch("app.main.valid_google_url")
        mock_valid_url.return_value = valid_url

        mock_has_connection = mocker.patch("app.main.has_internet_connection")
        mock_has_connection.return_value = has_connection

        assert can_access_google_page(self.url) == expected
