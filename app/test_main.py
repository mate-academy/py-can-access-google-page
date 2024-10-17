import pytest
from unittest import mock
from unittest.mock import MagicMock


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,mocked_result_connection,mocked_result_url,result",
    [
        ("http://google.com", True, True, "Accessible"),
        ("http://google.com", False, False, "Not accessible"),
        ("http://google.com", True, False, "Not accessible"),
        ("http://google.com", False, True, "Not accessible"),
    ],
    ids=[
        "return 'Accessible' connection is working, url is valid",
        "return 'Not accessible' connection is not working, url do not valid",
        "return 'Not accessible' connection is working, url do not valid",
        "return 'Not accessible' connection is not working, url is valid"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_exist(
        mocked_connection: MagicMock,
        mocked_url: MagicMock,
        url: str,
        mocked_result_connection: bool,
        mocked_result_url: bool,
        result: str
) -> None:
    can_access_google_page(url)
    mocked_connection.assert_called_once()
    mocked_url.assert_called_once()
    mocked_connection.return_value = mocked_result_connection
    mocked_url.return_value = mocked_result_url
    assert can_access_google_page(url) == result
