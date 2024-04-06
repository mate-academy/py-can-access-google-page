from unittest import mock
import pytest


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, valid_internet, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "access only with valid url and valid internet",
        "no access without internet",
        "no access without valid url",
        "no access without valid url and internet"
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        valid_internet: bool,
        expected_result: str
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        mocked_url.return_value = valid_url

        with mock.patch(
                "app.main.has_internet_connection"
        ) as mocked_connection:
            mocked_connection.return_value = valid_internet

            assert can_access_google_page(
                "https://www.google.com"
            ) == expected_result
