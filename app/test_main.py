from unittest import TestCase
from unittest.mock import patch

import pytest
from pytest import param

from app.main import can_access_google_page


class TestCanAccessGooglePage(TestCase):

    @pytest.mark.parametrize(
        "mock_has_internet, mock_valid_url, expected_result_param",
        [
            param(True, True, "Accessible", id="can_access_google_page test "),
            param(False, True, "Not accessible", id="no connection test "),
            param(True, False, "Not accessible", id="invalid url test "),
        ],
    )
    @patch("app.main.has_internet_connection", autospec=True)
    @patch("app.main.valid_google_url", autospec=True)
    def test_can_access_google_page(
            self,
            mock_has_internet: bool,
            mock_valid_url: bool,
            expected_result_param: str
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True

        result = can_access_google_page("http://www.google.com")
        self.assertEqual(result, expected_result_param)
