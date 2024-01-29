import pytest
from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage:

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    @pytest.mark.parametrize(
        "val1,val2,res",
        [
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (True, True, "Accessible"),
            (False, False, "Not accessible")
        ]
    )
    def test_should_return_valid_value(self,
                                       mocked_has_internet,
                                       mocked_valid_url,
                                       val1,
                                       val2,
                                       res):
        mocked_valid_url.return_value = val1
        mocked_has_internet.return_value = val2
        assert can_access_google_page("empty") == res
