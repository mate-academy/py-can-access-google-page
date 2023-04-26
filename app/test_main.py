import pytest

from unittest import mock

from app.main import can_access_google_page


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "has_internet_connection_result,valid_google_url_result",
        [
            pytest.param(
                False,
                True,
                id="should return 'Not accessible' when one func return False"
            ),
            pytest.param(
                True,
                False,
                id="should return 'Not accessible' when one func return False"
            ),
            pytest.param(
                False,
                False,
                id="should return 'Not accessible' when both func return False"
            )
        ]
    )
    def test_can_access_google_page_not_accessible(
            self,
            has_internet_connection_result: bool,
            valid_google_url_result: bool,
    ) -> None:
        with (
            mock.patch("app.main.has_internet_connection") as mocked_func1,
            mock.patch("app.main.valid_google_url") as mocked_func2
        ):
            mocked_func1.return_value = has_internet_connection_result
            mocked_func2.return_value = valid_google_url_result
            assert can_access_google_page("") == "Not accessible"

    def test_can_access_google_page_accessible(self) -> None:
        with (
            mock.patch("app.main.has_internet_connection") as mocked_func1,
            mock.patch("app.main.valid_google_url") as mocked_func2
        ):
            mocked_func1.return_value = True
            mocked_func2.return_value = True
            assert can_access_google_page("") == "Accessible"
