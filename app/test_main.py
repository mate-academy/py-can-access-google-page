import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection,validation_url,message_of_access",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Should be access to google page"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Should not be access, not valid url"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Should not be access, no internet connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Should not be access, not valid url and no internet connection"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_to_google_page(
        mock_connection: callable,
        mock_url: callable,
        internet_connection: bool,
        validation_url: bool,
        message_of_access: str
) -> None:
    mock_connection.return_value = internet_connection
    mock_url.return_value = validation_url
    assert can_access_google_page(
        url="https://www.google.com.ua/"
    ) == message_of_access
