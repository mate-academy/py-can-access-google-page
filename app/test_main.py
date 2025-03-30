import pytest

from app.main import can_access_google_page

from unittest.mock import patch


@pytest.fixture()
def mock_response() -> None:
    with patch("app.main.valid_google_url") as mock_response:
        yield mock_response


@pytest.fixture()
def mock_current_time() -> None:
    with patch("app.main.has_internet_connection") as mock_current_time:
        yield mock_current_time


@pytest.mark.parametrize(
    "response,current_time,expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id=("wen valid_google_url is 'True' and"
                "has_internet_connection is 'True',"
                "result must be 'Accessible'")
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id=("wen valid_google_url is 'False' and"
                "has_internet_connection is 'True',"
                "result must be 'Not accessible'")
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id=("wen valid_google_url is 'False' and"
                "has_internet_connection is 'False',"
                "result must be 'Not accessible'")
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id=("wen valid_google_url is 'True' and"
                "has_internet_connection is 'False',"
                "result must be 'Not accessible'")
        )
    ]
)
def test_can_access_google_page_correct_result(
        response: bool,
        current_time: bool,
        expected_result: str,
        mock_response: patch,
        mock_current_time: patch
) -> None:
    mock_response.return_value = response
    mock_current_time.return_value = current_time
    assert can_access_google_page("") == expected_result
