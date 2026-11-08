from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "url_valid,internet,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_all_combinations(
    url_valid: bool,
    internet: bool,
    expected: str
) -> None:
    with mock.patch(
        "app.main.valid_google_url", return_value=url_valid
    ), mock.patch(
        "app.main.has_internet_connection", return_value=internet
    ):
        assert main.can_access_google_page("https://google.com") == expected


def test_valid_google_url_should_be_called_with_given_url() -> None:
    with mock.patch(
        "app.main.valid_google_url", return_value=True
    ) as mocked_url, mock.patch(
        "app.main.has_internet_connection", return_value=True
    ):
        main.can_access_google_page("https://google.com")
        mocked_url.assert_called_once_with("https://google.com")
