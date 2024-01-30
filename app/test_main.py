import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection,valid_url,result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "without valid url func. should return 'Not accessible'",
        "without internet connect func. should return 'Not accessible'",
        "with internet connect AND valid url func. should return 'Accessible'"
    ]
)
def test_can_access_google_page(
        internet_connection: bool,
        valid_url: bool,
        result: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_valid,
          mock.patch("app.main.has_internet_connection") as mocked_connection):
        mocked_valid.return_value = internet_connection
        mocked_connection.return_value = valid_url
        assert can_access_google_page(url="https://www.google.com/") == result
