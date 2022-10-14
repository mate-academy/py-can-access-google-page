import pytest
from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "behaviors,result_expected",
        [
            pytest.param(
                [True, True],
                "Accessible",
                id="check access is allowed"
            ),
            pytest.param(
                [True, False],
                "Not accessible",
                id="check access not allowed (bad url)"
            ),
            pytest.param(
                [False, True],
                "Not accessible",
                id="check access not allowed (bad connection)"
            ),
            pytest.param(
                [False, False],
                "Not accessible",
                id="check access not allowed (bad everything)"
            )
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_check_function(self,
                            mocked_valid: object,
                            mocked_connection: object,
                            behaviors: list, result_expected: str) -> None:
        url = "https://www.google.com/"

        mocked_valid.return_value = behaviors[0]
        mocked_connection.return_value = behaviors[1]

        expected = can_access_google_page(url)

        mocked_connection.assert_called_once_with()
        if behaviors[1]:
            mocked_valid.assert_called_once_with(url)
        else:
            mocked_valid.assert_not_called()

        assert expected == result_expected
