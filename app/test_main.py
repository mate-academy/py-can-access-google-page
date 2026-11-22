from unittest import mock
import pytest


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, mocked_status_code, mocked_hour, expected_result", [
        pytest.param("https://www.google.com",
                     200,
                     12,
                     "Accessible",
                     id="Access Google page at midday."),
        pytest.param("https://www.google.com",
                     200,
                     23,
                     "Not accessible",
                     id="Access Google page at midnight."),
        pytest.param("https://www.googlecom",
                     400,
                     12,
                     "Not accessible",
                     id="Wrong url."),
    ]
)
@mock.patch("datetime.datetime")
@mock.patch("requests.get")
def test_can_access_google_page(
        mocked_get: mock.Mock,
        mocked_datetime: mock.Mock,
        url: str,
        mocked_status_code: int,
        mocked_hour: int,
        expected_result: str,
) -> None:
    mocked_get.return_value.status_code = mocked_status_code
    mocked_datetime.now.return_value.hour = mocked_hour
    assert can_access_google_page(url) == expected_result
