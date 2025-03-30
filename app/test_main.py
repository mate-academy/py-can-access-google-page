import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, expect_result",
    [
        pytest.param(True, True, "Accessible"),
        pytest.param(True, False, "Not accessible"),
        pytest.param(False, True, "Not accessible"),
        pytest.param(False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google_url: mock.MagicMock,
                                mock_has_internet_connection: mock.MagicMock,
                                internet_connection: bool,
                                valid_url: bool,
                                expect_result: str
                                ) -> None:

    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection

    assert can_access_google_page("www.google.com") == expect_result
