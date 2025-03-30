from unittest import mock

import pytest

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "has_connection, valid_url, result",
        [
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (True, True, "Accessible"),
            (False, False, "Not accessible")
        ]
    )
    def test_can_access_google_page(
            self,
            has_connection: bool,
            valid_url: bool,
            result: str

    ) -> None:
        with (
            mock.patch(
                "app.main.has_internet_connection", return_value=has_connection
            ),
            mock.patch(
                "app.main.valid_google_url", return_value=valid_url
            )
        ):
            assert can_access_google_page("https://mate.academy/en") == result
