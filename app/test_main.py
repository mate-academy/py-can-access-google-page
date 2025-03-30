import pytest
from unittest import mock
from requests.exceptions import (
    MissingSchema,
    ConnectionError,
    InvalidURL
)

from app.main import can_access_google_page, valid_google_url


@mock.patch("app.main.valid_google_url")
def test_should_return_valid_url(
        mocked_valid_url: any
) -> None:
    can_access_google_page("http://google.com")

    mocked_valid_url.assert_called_once()


@mock.patch("app.main.has_internet_connection")
def test_should_return_internet_connection(
        mock_internet_connection: any
) -> None:
    can_access_google_page("http://google.com")

    mock_internet_connection.assert_called_once()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "initial_url,initial_hour,expected_result",
    [
        pytest.param(
            "http://google.com",
            True,
            "Accessible",
            id="check valid url and right hour"
        ),
        pytest.param(
            "http://google.com",
            False,
            "Not accessible",
            id="hour has to be from 6 to 22"
        ),
        (
            "https://translate.google.com/",
            False,
            "Not accessible"
        )
    ]
)
def test_can_access_google_page(
        mocked_url: mock.MagicMock,
        mocked_time: mock.MagicMock,
        initial_url: str,
        initial_hour: bool,
        expected_result: bool
) -> None:
    mocked_time.return_value = initial_hour
    mocked_url.return_value = initial_url

    assert can_access_google_page(mocked_url) == expected_result


@pytest.mark.parametrize(
    "initial_element,expected_error",
    [
        pytest.param(
            "http://google",
            ConnectionError,
            id="url has to have a scheme - `http://[name_of_site].[domain]`"
        ),
        pytest.param(
            "http://",
            InvalidURL,
            id="url don't have all body - `http://[name_of_site].[domain]`"
        ),
        pytest.param(
            4,
            MissingSchema,
            id="url has to have type of string"
        ),
        pytest.param(
            "",
            MissingSchema,
            id="empty sting is not a valid url"
        ),

    ]
)
def test_should_return_error_when_ulr_invalid(
        initial_element: any,
        expected_error: any,
) -> None:
    with pytest.raises(expected_error):
        raise valid_google_url(initial_element)
