import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,has_internet,valid_url,expected_result",
    [
        ("https://www.google.com/", True, True, "Accessible"),
        ("https://www.12345.gh", False, True, "Not accessible"),
        ("https://--//.uk", True, False, "Not accessible"),
        ("https://hello.ukkjh", False, False, "Not accessible"),

    ],
    ids=[
        "Should return 'Accessible' if there is internet and url is valid",
        "Should return 'Not accessible' "
        "if there is no internet and url is valid",
        "Should return 'Not accessible' "
        "if there is internet but url isn't valid",
        "Should return 'Accessible' "
        "if there is no internet and url is not valid"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_that_must_return_correct_result(
        mocked_has_internet_connection: mock.MagicMock,
        mocked_valid_google_url: mock.MagicMock,
        url: str,
        valid_url: bool,
        has_internet: bool,
        expected_result: str,
) -> None:
    mocked_has_internet_connection.return_value = has_internet
    mocked_valid_google_url.return_value = valid_url
    assert can_access_google_page(url) == expected_result
