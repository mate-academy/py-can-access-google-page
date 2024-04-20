import app.main
from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.fixture()
def mocking_functions() -> None:
    app.main.valid_google_url = mock.MagicMock()
    app.main.has_internet_connection = mock.MagicMock()


@pytest.mark.parametrize(
    "valid_url,connection,result",
    [
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test fails if url is not valid"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test fails if connection fails"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="test fails if both params fail"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="test success if both params success"
        )
    ]
)
def test(mocking_functions: callable,
         valid_url: bool,
         connection: bool,
         result: str) -> None:
    link = "some_link"
    app.main.valid_google_url.return_value = valid_url
    app.main.has_internet_connection.return_value = connection
    assert can_access_google_page(link) == result
