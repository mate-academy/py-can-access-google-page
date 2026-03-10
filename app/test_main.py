import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "initial_internet, initial_url, expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="should return 'Accessible' if are internet and correct url"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="should return 'Not accessible' if is not correct url"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="should return 'Not accessible' if is not internet"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="should return 'Not accessible' if are not internet and correct url"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_scenarios(
        mock_internet: bool,
        mock_url: bool,
        initial_internet: bool,
        initial_url: bool,
        expected: str,
) -> None:

    mock_internet.return_value = initial_internet
    mock_url.return_value = initial_url

    result = can_access_google_page("google.com")
    assert result == expected
