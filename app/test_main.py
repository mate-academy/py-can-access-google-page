import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid,is_connection,accessibility",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="valid and connection is 'True'"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="valid is 'False', but connection is 'True'"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="valid is 'True', but connection is 'False'"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="valid and connection is 'False'"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_can_access_google_page(
        mock_valid: mock.Mock,
        mock_connection: mock.Mock,
        is_valid: bool,
        is_connection: bool,
        accessibility: str
) -> None:
    mock_valid.return_value = is_valid
    mock_connection.return_value = is_connection
    assert can_access_google_page("https://www.some_url.com/") == accessibility