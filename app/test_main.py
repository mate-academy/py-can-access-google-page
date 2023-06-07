import pytest
from unittest import mock
from app import main
from app.main import has_internet_connection, valid_google_url


@pytest.mark.parametrize("mock_valid_google, mock_has_internet, expected_result", [
    (mock.Mock(return_value=True), mock.Mock(return_value=True), True),
    (mock.Mock(return_value=False), mock.Mock(return_value=True), True),
    (mock.Mock(return_value=True), mock.Mock(return_value=False), True),
    (mock.Mock(return_value=False), mock.Mock(return_value=False), True),
])
def test_has_internet_connection(mock_valid_google, mock_has_internet, expected_result):
    # Patching the functions with the mock objects
    with mock.patch("app.main.valid_google_url", mock_valid_google), \
            mock.patch("app.main.has_internet_connection", mock_has_internet):
        # Set the side effect for mock_has_internet
        result = has_internet_connection()

        # Assert the result
        assert result == expected_result


def test_cannot_access_if_connection_or_valid_url_is_true(monkeypatch):
    def can_access_if_connection_or_valid_url(url):
        from app.main import has_internet_connection, valid_google_url

        if has_internet_connection() or valid_google_url(url):
            return "Accessible"
        else:
            return "Not accessible"

    monkeypatch.setattr(main, "can_access_google_page", can_access_if_connection_or_valid_url)

    result = test_has_internet_connection()
    assert result.value == 0, "You cannot access page if only one of 'connection' or 'valid url' is True."
