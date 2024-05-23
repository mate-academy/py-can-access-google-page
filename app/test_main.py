from unittest import mock

import pytest

from app.main import can_access_google_page


def test_with_called_functions() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_internet,
        mock.patch("app.main.valid_google_url") as mocked_url_validation
    ):
        can_access_google_page("f")
        mocked_internet.assert_called_once()
        mocked_url_validation.assert_called_once_with("f")


def test_with_returned_false_by_inner_function_1() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_internet,
        mock.patch("app.main.valid_google_url") as mocked_url_validation
    ):
        mocked_internet.return_value = False
        mocked_url_validation.return_value = True
        assert can_access_google_page("") == "Not accessible"


def test_with_returned_false_by_inner_function_2() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_internet,
        mock.patch("app.main.valid_google_url") as mocked_url_validation
    ):
        mocked_internet.return_value = True
        mocked_url_validation.return_value = False
        assert can_access_google_page("") == "Not accessible"


@pytest.mark.parametrize(
    "url,expected",
    [
        ("bad_url", Exception),
    ]
)
def test_exception_rising(
        url: str,
        expected: type(Exception)
) -> None:
    with pytest.raises(expected):
        can_access_google_page(url)
