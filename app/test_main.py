from app.main import can_access_google_page
from pytest import mark
from unittest import mock


@mark.parametrize(
    "url,has_connection,valid_url,expected_output",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://zweeqf.com", True, False, "Not accessible"),
        ("https://xcbvn.com", False, True, "Not accessible"),
        ("https://xcbvncom", False, False, "Not accessible"),
    ],
    ids=[
        "Must return 'Accessible', if you have internet and URL is valid",
        "Must return 'Not accessible', if URL is not valid",
        "Must return 'Not accessible', if you don't have internet",
        ("Must return 'Not accessible', if you don't have internet"
         " and URL isn't valid"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_return_correct_output(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        url: str,
        valid_url: bool,
        has_connection: bool,
        expected_output: str
) -> None:
    mocked_has_internet_connection.return_value = has_connection
    mocked_valid_google_url.return_value = valid_url
    assert can_access_google_page(url) == expected_output
