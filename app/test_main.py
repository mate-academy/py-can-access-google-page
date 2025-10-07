import pytest
from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "vgu_return_value,"
        "hic_return_value,"
        "expected_result",
        [
            pytest.param(
                True, True, "Accessible",
                id="should return 'Accessible' when both True"
            ),
            pytest.param(
                False, True, "Not accessible",
                id="should return 'Not accessible' when invalid Google url"
            ),
            pytest.param(
                True, False, "Not accessible",
                id="should return 'Not accessible' when no internet connection"
            ),
            pytest.param(
                False, False, "Not accessible",
                id="should return 'Not accessible' when both False"
            )
        ]

    )
    def test_should_return_correct_bool(
            self,
            vgu_return_value: bool,
            hic_return_value: bool,
            expected_result: str
    ) -> None:
        with (
            mock.patch("app.main.valid_google_url")
            as valid_google_url,
            mock.patch("app.main.has_internet_connection")
            as has_internet_connection
        ):
            valid_google_url.return_value = vgu_return_value
            has_internet_connection.return_value = hic_return_value
            assert can_access_google_page("") == expected_result
