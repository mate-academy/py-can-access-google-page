from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import can_access_google_page


url = "https://google.com"

@pytest.mark.parametrize(
    "mocked_url_return_value,"
    "mocked_connection_return_value,"
    "expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id = "should return `Accessible` "
                 "if both mocked values are `True`"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id = "should return `Not accessible` "
                 "if connection mocked value is `False`"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id = "should return `Not accessible` "
                 "if url mocked value is `False`"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id = "should return `Not accessible` "
                 "if both mocked values are `False`"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_with_mocked_different_dependencies(
    mocked_url: MagicMock,
    mocked_connection: MagicMock,
    mocked_url_return_value: bool,
    mocked_connection_return_value: bool,
    expected_result: str
) -> None:
    mocked_url.return_value = mocked_url_return_value
    mocked_connection.return_value = mocked_connection_return_value

    assert can_access_google_page(url) == expected_result
