import pytest
from app.main import can_access_google_page
from unittest import mock


# class TestResponse:
#     def __init__(self, code: int) -> None:
#         self.status_code = code
#
#
# class TestDatetime:
#     def __init__(self, hour: int) -> None:
#         self.hour = hour


@pytest.mark.parametrize(
    "is_valid_url,is_connection,result",
    [
        (True, True, "Accessible"),
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access(
        is_valid_url: int,
        is_connection: int,
        result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_url,
        mock.patch("app.main.has_internet_connection") as mocked_connection
    ):
        mocked_url.return_value = is_valid_url
        mocked_connection.return_value = is_connection
        assert can_access_google_page("some_url") == result
