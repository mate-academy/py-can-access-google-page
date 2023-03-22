import pytest

from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_url,internet_connection,expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="URL is valid, has internet connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="URL not valid, has internet connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="URL is valid, no internet connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="URL not valid, no internet connection"
        ),
    ]
)
def test_can_access_google_page(
        mocked_valid_url: mock.Mock,
        mocked_internet_connection: mock.Mock,
        valid_url: bool,
        internet_connection: bool,
        expected: str,
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = internet_connection
    assert (
        can_access_google_page("test_url") == expected
    )


# def test_can_access_google_page(
#         valid_url: bool,
#         internet_connection: bool,
#         expected: str) -> None:
#     with (mock.patch("app.main.valid_google_url") as mocked_valid_google_url,
#           mock.patch("app.main.has_internet_connection") as
#           mocked_has_internet_connection):
#         mocked_valid_google_url.return_value = valid_url
#         mocked_has_internet_connection.return_value = internet_connection
#         assert (
#             can_access_google_page("test_url") == expected
#         )
