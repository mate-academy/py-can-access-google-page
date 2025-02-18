from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_valid_url,mock_internet_connection, expected_result",
    [
        pytest.param(
            True, True, "Accessible",
            id="should return 'Accessible' when both function 'True'"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="should return 'Not accessible'"
               " when mock_internet_connection 'False'"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="should return 'Not accessible' when mock_valid_url 'False'"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="should return ' Not accessible' when both function 'False'"
        )
    ]
)
def test_can_access_google_page(
        mock_valid_url: bool,
        mock_internet_connection: bool,
        expected_result: str
) -> None:
    with mock.patch(
            "app.main.valid_google_url",
            return_value=mock_valid_url
    ), mock.patch(
            "app.main.has_internet_connection",
            return_value=mock_internet_connection
    ):
        assert can_access_google_page(
            "https://www.google.com"
        ) == expected_result
