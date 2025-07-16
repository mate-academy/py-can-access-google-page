from app.main import can_access_google_page
from unittest import mock
import datetime


def test_return_string() -> None:
    result = can_access_google_page("https://www.youtube.com/")
    assert isinstance(result, str)


def test_working_url() -> None:
    assert can_access_google_page("https://www.youtube.com/") == "Accessible"


def test_input_invalid_url() -> None:
    assert (can_access_google_page
            ("https://www.youtube.com/fjwpuifpiuwefpoiw") == "Not accessible")


@mock.patch("datetime.datetime")
def test_if_one_of_function_is_false(mock_time: datetime) -> None:

    mock_time.datetime.now.return_value = (
        datetime.datetime(2000, 1, 1, 0, 0, 0))

    assert (can_access_google_page("https://www.youtube.com/")
            == "Not accessible")
