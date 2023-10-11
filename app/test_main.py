from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize("test_bool_url, test_bool_internet, result", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
    (False, False, "Not accessible")
])
def test_can_access_google_page_false(
        test_bool_url: bool,
        test_bool_internet: bool,
        result: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_bool_url,
          mock.patch("app.main.has_internet_connection") as mocked_bool_internet):
        mocked_bool_url.return_value = test_bool_url
        mocked_bool_internet.return_value = test_bool_internet
        assert can_access_google_page(str(mocked_bool_url)) == result
