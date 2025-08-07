import pytest
from app.main import can_access_google_page
from unittest import mock


class TestResponse:
    def __init__(self, code: int) -> None:
        self.status_code = code


class TestDatetime:
    def __init__(self, hour: int) -> None:
        self.hour = hour


@pytest.mark.parametrize(
    "test_hour,test_code,result",
    [
        (15, 200, "Accessible"),
        (22, 200, "Accessible"),
        (5, 200, "Not accessible"),
        (23, 200, "Not accessible"),
        (15, 404, "Not accessible"),
        (2, 500, "Not accessible"),
    ]
)
def test_can_access_if_both_true(
        test_hour: int,
        test_code: int,
        result: str
) -> None:
    with (
        mock.patch("datetime.datetime") as mocked_dtt,
        mock.patch("requests.get") as mocked_get
    ):
        mocked_dtt.now.return_value = TestDatetime(test_hour)
        mocked_get.return_value = TestResponse(test_code)
        assert can_access_google_page("some_url") == result
