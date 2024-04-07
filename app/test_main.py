from unittest.mock import patch, MagicMock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_url,is_internet,expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "return 'Accessible' if url is valid and there is internet access",
        "return 'Not accessible' if url is not valid",
        "return 'Not accessible' if there is no internet",
        "return 'Not accessible' if url is not valid and there is no internet",
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_internet_func: MagicMock,
    mocked_url_func: MagicMock,
    is_internet: bool,
    is_url: bool,
    expected: str
) -> None:
    mocked_internet_func.return_value = is_internet
    mocked_url_func.return_value = is_url
    assert can_access_google_page("url") == expected


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
class TestInternalFuncCalled:
    def test_has_internet_connection_called(
        self,
        mocked_internet_func: MagicMock,
        mocked_url_func: MagicMock
    ) -> None:
        can_access_google_page("url")
        mocked_internet_func.assert_called_once()

    def test_valid_google_url_called(
        self,
        mocked_internet_func: MagicMock,
        mocked_url_func: MagicMock
    ) -> None:
        can_access_google_page("url")
        mocked_url_func.assert_called_once()
