import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_result,internet_connection,result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ],
    ids=[
        "Success, you can access google page.",
        "Fail, you can`t access google page.",
        "Check your url, it must be wrong.",
        "Check your internet connection."
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: mock,
        valid_result: bool,
        internet_connection: bool,
        result: str
) -> None:
    mocked_valid_google_url.return_value = valid_result
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://mate.academy/en") == result
