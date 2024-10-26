from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_value,connection_value,result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="can access google page if 2 value true"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="can access google page if valid value true"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="can access google page if 2 value false"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="can access google page if connection value true"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid: Mock,
        mock_has_internet: Mock,
        valid_value: bool,
        connection_value: bool,
        result: str
) -> None:
    mock_valid.return_value = valid_value
    mock_has_internet.return_value = connection_value
    assert can_access_google_page("test") == result
