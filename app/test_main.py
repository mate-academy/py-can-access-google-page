from unittest import mock
from unittest.mock import patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "status,internet,result",
    [
        (True, False, "Not accessible"),
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible")
    ],
    ids=[
        "test access google page fail correct url night time",
        "test access google page success correct url day time",
        "test access google page fail wrong url night time",
        "test access google page fail wrong url day time"
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_access_google_page(
        mocked_has_internet_connection: mock,
        mocked_valid_google_url: mock,
        status: bool,
        internet: bool,
        result: str
) -> None:
    mocked_valid_google_url.return_value = status
    mocked_has_internet_connection.return_value = internet

    assert can_access_google_page("not matter") == result
