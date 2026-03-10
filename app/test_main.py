import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "initial_internet, initial_url, expected",
    [
        pytest.param(
            True, True, True,
            id="should return True if are internet and correct url"
        ),
        pytest.param(
            True, False, False,
            id="should return False if is not correct url"
        ),
        pytest.param(
            False, True, False,
            id="should return False if is not internet"
        ),
        pytest.param(
            False, False, False,
            id="should return False if are not internet and correct url"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_access_to_url(
        mock_internet: bool,
        mock_url: bool,
        initial_internet: bool,
        initial_url: bool,
        expected: bool,
) -> None:

    mock_internet.return_value = initial_internet
    mock_url.return_value = initial_url

    result = can_access_google_page("google.com")
    assert result == expected
