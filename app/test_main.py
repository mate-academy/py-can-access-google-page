import pytest
from unittest import mock

from app.main import can_access_google_page


test_url = "url"


@pytest.fixture
def mocked_request_url_response() -> callable:
    with mock.patch(
        "app.main.valid_google_url"
    ) as mocked_url_response:
        yield mocked_url_response


@pytest.fixture
def mocked_connection_availability() -> callable:
    with mock.patch(
        "app.main.has_internet_connection"
    ) as mocked_connection_response:
        yield mocked_connection_response


@pytest.mark.parametrize(
    "connection_response, url_response, expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="succesful access if google url is valid\
                 and internet connection is available"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="not accessible if internet connection is unavailable"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="not accessible if url response is invalid"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="not accessible if url response is invalid\
                 and internet connection is unavailable"
        )
    ]
)
def test_access_to_google_page(
    connection_response: bool,
    url_response: bool,
    expected_result: str,
    mocked_request_url_response: callable,
    mocked_connection_availability: callable
) -> None:
    mocked_request_url_response.return_value = url_response
    mocked_connection_availability.return_value = connection_response

    assert can_access_google_page(test_url) == expected_result
