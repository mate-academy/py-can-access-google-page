from unittest import mock
import datetime
import pytest

from app.main import has_internet_connection
from app.main import valid_google_url
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "value,expect_result",
    [
        pytest.param(
            datetime.datetime(
                year=2023,
                month=6,
                day=20,
                hour=4
            ),
            False,
            id="internet_connection_not_allowed"
        ),
        pytest.param(
            datetime.datetime(
                year=2023,
                month=6,
                day=20,
                hour=10
            ),
            True,
            id="internet_connection_allowed"
        )
    ]
)
@mock.patch("datetime.datetime")
def test_internet_connection(mock_datetime: mock,
                             value: datetime,
                             expect_result: bool) -> None:
    mock_datetime.now.return_value = value
    assert has_internet_connection() is expect_result
    print(mock_datetime.datetime.now.return_value)
    print(has_internet_connection())
    print(expect_result)


@pytest.mark.parametrize(
    "value_code,expect_result",
    [
        pytest.param(
            200, True, id="valid url"
        ),
        pytest.param(
            404, False, id="not valid url"
        )
    ]
)
@mock.patch("requests.get")
def test_valid_google_url(mock_requests_get: mock,
                          value_code: int,
                          expect_result: bool) -> None:
    site = "https://www.google.com"
    mock_response = mock.MagicMock()
    mock_response.status_code = value_code
    mock_requests_get.return_value = mock_response
    assert valid_google_url(site) == expect_result


@pytest.mark.parametrize(
    "valid_url,has_connection,expect_value",
    [
        pytest.param(
            True, True, "Accessible", id="has access to page"
        ),
        pytest.param(
            True, False, "Not accessible", id="access is not allowed"
        ),
        pytest.param(
            False, True, "Not accessible", id="access is not allowed"
        ),
        pytest.param(
            False, False, "Not accessible", id="access is not allowed"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_google_url: mock,
                                mock_has_internet_connection: mock,
                                valid_url: bool,
                                has_connection: bool,
                                expect_value: str) -> None:
    site = "https://www.google.com"
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_connection

    assert can_access_google_page(site) == expect_value
