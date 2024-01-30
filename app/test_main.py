import pytest
from unittest import mock

from app.main import can_access_google_page


PATH = "app.main"


@pytest.mark.parametrize(
    "url, valid_url_result, current_time, expected_result",
    [
        pytest.param("https://google.com/", True, True, "Accessible",
                     id="We should return Accessible if url is valid "
                        "and allowable current time"),

        pytest.param("https://www.youtube.com/", False, True, "Not accessible",
                     id="We should return Not accessible if got invalid url"),

        pytest.param("https://google.com/", True, False, "Not accessible",
                     id="We should return Not accessible "
                        "if got not allowable current time")
    ]
)
def test_can_access_google_page(
        url: str,
        valid_url_result: bool,
        current_time: bool,
        expected_result: str
) -> None:
    with mock.patch(f"{PATH}.valid_google_url") as mock_valid_google_url, \
         mock.patch(f"{PATH}.has_internet_connection") as mock_time_connection:
        mock_valid_google_url.return_value = valid_url_result
        mock_time_connection.return_value = current_time
        assert can_access_google_page(url) == expected_result
