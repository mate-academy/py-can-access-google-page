from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    (
        "url,"
        "return_value_valid_google_url,"
        "return_value_has_internet_connection,"
        "expected"
    ),
    [
        ("google.com", True, True, "Accessible"),
        ("google.com", True, False, "Not accessible"),
        ("wrong_url.com", False, True, "Not accessible"),
        ("wrong_url.com", False, False, "Not accessible")
    ],
    ids=[
        "valid url + internet",
        "valid url + no internet",
        "invalid url + internet",
        "invalid ulr + no internet"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_has_internet_connection: mock.MagicMock,
    mocked_valid_google_url: mock.MagicMock,
    url: str,
    return_value_valid_google_url: bool,
    return_value_has_internet_connection: bool,
    expected: str
) -> None:
    mocked_valid_google_url.return_value = return_value_valid_google_url
    mocked_has_internet_connection.return_value = (
        return_value_has_internet_connection
    )

    result = can_access_google_page(url)

    assert result == expected
    mocked_has_internet_connection.assert_called_once_with()
    if return_value_has_internet_connection:
        mocked_valid_google_url.assert_called_once_with(url)
