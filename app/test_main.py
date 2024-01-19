import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "url,valid_url,has_internet,expected_output",
    [
        ("www.google.com", True, True, "Accessible"),
        ("www.gоogle.com", False, True, "Not accessible"),
        ("www.google.com", True, False, "Not accessible"),
        ("www.gologle.com", False, False, "Not accessible")
    ],
    ids=[
        "Test for 'Accessible' with correct values",
        "Test for 'Not accessible' with a cyrillic typo in url",
        "Test for 'Not accessible' with no connection",
        "Test for 'Not accessible' with wrong link and no connection"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_correct_google_access_message(
        mocked_internet: mock.MagicMock,
        mocked_url: mock.MagicMock,
        url: str,
        valid_url: bool,
        has_internet: bool,
        expected_output: str
) -> None:
    mocked_url.return_value = valid_url
    mocked_internet.return_value = has_internet
    assert can_access_google_page(url) == expected_output
