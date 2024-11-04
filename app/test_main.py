import pytest
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_cannot_access_if_only_valid_url(mock_valid_google_url, mock_has_internet_connection):
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_cannot_access_if_only_connection(mock_valid_google_url, mock_has_internet_connection):
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_can_access_if_both_conditions_true(mock_valid_google_url, mock_has_internet_connection):
    assert can_access_google_page("https://google.com") == "Accessible"

@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_cannot_access_if_both_conditions_false(mock_valid_google_url, mock_has_internet_connection):
    assert can_access_google_page("https://google.com") == "Not accessible"


if __name__ == "__main__":
    pytest.main()
