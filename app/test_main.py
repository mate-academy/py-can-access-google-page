from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page


class TestCanAccessPage:
    @pytest.mark.parametrize(
        "connection,valid,access",
        [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible")
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_valid_googl_url_and_has_internet_connection(
            self,
            mock_check_valid: Callable,
            mock_check_connection: Callable,
            connection: bool,
            valid: bool,
            access: str
    ) -> None:
        mock_check_valid.return_value = valid
        mock_check_connection.return_value = connection
        assert can_access_google_page("www.googl.com") == access
# write your code here
