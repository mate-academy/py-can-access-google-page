import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_validation, connection_validation, status",
    [
        pytest.param(False, True, "Accessible", id="Test all correct value"),
        pytest.param(True, False, "Not accessible", id="Test all correct url"),
        pytest.param(False,
                     True,
                     "Not accessible",
                     id="Test all correct time"),
        pytest.param(
            False, False, "Not accessible", id="Test all correct url and time"
        ),
    ],
)
def test_can_access_google_page(
    url_validation: bool, connection_validation: bool, status: str
) -> None:
    with mock.patch(
        "app.main.valid_google_url", return_value=url_validation
    ), mock.patch(
        "app.main.has_internet_connection", return_value=connection_validation
    ):
        assert (
            can_access_google_page(
                "https://www.google.com/search?q=mate+academy&oq=mate+academy"
            )
            == status
        )
