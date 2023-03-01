from unittest import mock

import pytest

from app.main import can_access_google_page

URL_GOOGLE = "https://www.google.com"


@pytest.fixture()
def mocked_validations() -> mock.Mock:
    with (
        mock.patch("app.main.valid_google_url") as mock_url,
        mock.patch("app.main.has_internet_connection") as mock_connection
    ):
        yield mock_url, mock_connection


def test_valid_url_and_connection(
        mocked_validations: mock
) -> None:
    mocked_validations[0].return_value = True
    mocked_validations[1].return_value = True
    assert can_access_google_page(URL_GOOGLE) == "Accessible"


def test_bad_connection(
        mocked_validations: mock
) -> None:
    mocked_validations[0].return_value = False
    mocked_validations[1].return_value = True
    assert can_access_google_page(URL_GOOGLE) == "Not accessible"


def test_no_connection(
        mocked_validations: mock
) -> None:
    mocked_validations[0].return_value = True
    mocked_validations[1].return_value = False
    assert can_access_google_page(URL_GOOGLE) == "Not accessible"


def test_not_valid_connection_and_url(
        mocked_validations: mock
) -> None:
    mocked_validations[0].return_value = False
    mocked_validations[1].return_value = False
    assert can_access_google_page(URL_GOOGLE) == "Not accessible"
