import pytest
from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_google_url_value,internet_connection_value,return_value",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id='Should return \"Accessible\" if all True'
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id='Should return \"Not accessible\" if one param is False'
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id='Should return \"Not accessible\" if one param is False'
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id='Should return \"Not accessible\" if one param is False'
        )
    ]
)
def test_can_access_google_page(
        mock_valid_google_url: callable,
        mock_has_internet_connection: callable,
        valid_google_url_value: bool,
        internet_connection_value: bool,
        return_value: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url_value
    mock_has_internet_connection.return_value = internet_connection_value
    assert can_access_google_page("_") == return_value
