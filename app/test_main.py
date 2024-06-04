from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url() -> object:
    with (mock.patch("app.main.valid_google_url")) as mock_valid:
        yield mock_valid


@pytest.fixture
def mock_has_internet_connection() -> object:
    with (mock.patch("app.main.has_internet_connection")) as mock_connection:
        yield mock_connection


@pytest.mark.parametrize(
    "init_mock_valid, init_mock_has_internet, init_str, result",
    [
        pytest.param(
            True,
            True,
            "Test",
            "Accessible",
            id="test_can_access_google_page_accsesible",

        ),
        pytest.param(
            True,
            False,
            "",
            "Not accessible",
            id="test_can_access_google_page_not_accsesible_1_0",

        ),
        pytest.param(
            False,
            True,
            "",
            "Not accessible",
            id="test_can_access_google_page_not_accsesible_0_1",

        ),
        pytest.param(
            False,
            False,
            "",
            "Not accessible",
            id="test_can_access_google_page_not_accsesible_0_0",

        ),

    ]
)
def test_can_access(
        mock_valid_google_url: object,
        mock_has_internet_connection: object,
        init_mock_valid: bool,
        init_mock_has_internet: bool,
        init_str: str,
        result: str

) -> None:
    mock_valid_google_url.return_value = init_mock_valid
    mock_has_internet_connection.return_value = init_mock_has_internet

    assert can_access_google_page(init_str) == result
