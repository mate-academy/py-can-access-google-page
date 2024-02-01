from unittest import mock

from pytest import mark, param

from app.main import can_access_google_page


PATH = "app.main"


@mark.parametrize(
    "valid_url_result, current_time, expected_result",
    [
        param(True, True, "Accessible",
              id="Should return Accessible if url is valid and allowable current time"),

        param( False, True, "Not accessible",
              id="Should return Not accessible if got invalid url"),

        param(True, False, "Not accessible",
              id="Should return Not accessible if time is not allowable"),
        param( False, False, "Not accessible",
              id="Should return Not accessible if time is not allowable "
                 "and if url is invalid")

    ]
)
def test_can_access_google_page(
        valid_url_result: bool,
        current_time: bool,
        expected_result: str
) -> None:
    with mock.patch(f"{PATH}.valid_google_url") as mock_valid_google_url:
        with mock.patch(f"{PATH}.has_internet_connection") as mock_time_connection:
            mock_valid_google_url.return_value = valid_url_result
            mock_time_connection.return_value = current_time
            assert can_access_google_page("some_url_from_testcase") == expected_result
