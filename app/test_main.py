from unittest.mock import patch, MagicMock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def url() -> str:
    return "https://fakeurl"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
class TestCanAccessGooglePageFunc:
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
            "return 'Not accessible' if url is not valid and there is no "
            "internet",
        ]
    )
    def test_function_should_return_correct_value(
        self,
        mocked_internet_func: MagicMock,
        mocked_url_func: MagicMock,
        is_internet: bool,
        is_url: bool,
        expected: str,
        url: str,
    ) -> None:
        mocked_internet_func.return_value = is_internet
        mocked_url_func.return_value = is_url
        assert can_access_google_page(url) == expected

    @pytest.mark.parametrize(
        "is_url,is_internet,expected",
        [
            (True, True, 2),
            (False, True, 1),
            (True, False, 1),
            (False, False, 1)
        ],
        ids=[
            "'valid_google_url' and 'has_internet_connection' "
            "should have been called once",
            "'valid_google_url' or 'has_internet_connection' "
            "should have been called once",
            "'valid_google_url' or 'has_internet_connection' "
            "should have been called once",
            "'valid_google_url' or 'has_internet_connection' "
            "should have been called once",
        ]
    )
    def test_other_functions_have_been_called(
        self,
        mocked_internet_func: MagicMock,
        mocked_url_func: MagicMock,
        is_internet: bool,
        is_url: bool,
        expected: int,
        url: str,
    ) -> None:
        mocked_internet_func.return_value = is_internet
        mocked_url_func.return_value = is_url
        can_access_google_page(url)
        assert mocked_internet_func.called + mocked_url_func.called >= expected
