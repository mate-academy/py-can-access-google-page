from unittest import monk
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_validation, internet_connection, access_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@monk.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: bool,
        mock_valid_url: bool,
        url_validation: bool,
        internet_connection: bool,
        access_resul: str
) -> None:
    mock_has_internet.return_value = internet_connection
    mock_valid_url.return_value = url_validation

    assert can_access_google_page("url") ==access_result
