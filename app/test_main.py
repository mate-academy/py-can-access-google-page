import pytest

from unittest import mock
from typing import Iterator

from app.main import can_access_google_page


@pytest.fixture()
def mock_internet() -> Iterator[mock.MagicMock]:
    with mock.patch("app.main.has_internet_connection") as patched:
        yield patched


@pytest.fixture()
def mock_url() -> Iterator[mock.MagicMock]:
    with mock.patch("app.main.valid_google_url") as patched:
        yield patched


@pytest.mark.parametrize(
    "valid_url,internet,expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="test_url_and_internet_values_are_valid"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="test_url_and_internet_values_are_invalid"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test_url_value_is_valid_and_internet_value_is_invalid"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test_url_value_is_invalid_and_internet_value_is_valid"
        )
    ]
)
def test_program_with_different_values(
        valid_url: bool,
        internet: bool,
        expected: str,
        mock_internet: mock.MagicMock,
        mock_url: mock.MagicMock
) -> None:
    mock_internet.return_value = internet
    mock_url.return_value = valid_url

    result = can_access_google_page("https://mate.academy/")
    assert result == expected
