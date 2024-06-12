from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "func1_res,func2_res,final_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_connection_exists_and_url_is_valid(
        func1_res: bool,
        func2_res: bool,
        final_result: str
) -> None:
    with (mock.patch("app.main.has_internet_connection") as mocked_connection,
          mock.patch("app.main.valid_google_url") as mocked_url_validation):
        mocked_connection.return_value = func1_res
        mocked_url_validation.return_value = func2_res
        assert can_access_google_page("https://github.com") == final_result
