import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_valid_url,mock_internet_connection,expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should return 'accessible' with vu and ic",
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should return 'not accessible' with iu and ic",
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should return 'not accessible' with vu and no ic",
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should return 'not accessible' with iu and no ic",
        ),
    ]
)
def test_can_access_google_page(
        mock_valid_url: bool,
        mock_internet_connection: bool,
        expected: str
) -> None:
    with mock.patch(
            "app.main.valid_google_url",
            return_value=mock_valid_url
    ):
        with mock.patch(
                "app.main.has_internet_connection",
                return_value=mock_internet_connection
        ):
            assert can_access_google_page("https://www.google.com") == expected
