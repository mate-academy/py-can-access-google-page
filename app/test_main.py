import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, value, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_function(
        mocked_connection: None,
        mocked_url: None,
        url: bool,
        value: bool,
        result: str
) -> None:
    mocked_url.return_value = url
    mocked_connection.return_value = value

    assert can_access_google_page("mate.academy") == result
