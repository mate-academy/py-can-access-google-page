from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


# We use patch to replace the functions in the "main" module during the test
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_success(
    mock_valid: MagicMock, mock_internet: MagicMock
) -> None:
    """Test scenario: Both internet and URL are valid."""
    # Arrange: Set the return values for the mocks
    mock_internet.return_value = True
    mock_valid.return_value = True

    # Act: Call the function under test
    result = can_access_google_page("https://google.com")

    # Assert: Verify the outcome and that mocks were called correctly
    assert result == "Accessible"
    mock_internet.assert_called_once()
    mock_valid.assert_called_once_with("https://google.com")


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_no_internet(
    mock_valid: MagicMock, mock_internet: MagicMock
) -> None:
    """Test scenario: URL is valid but there is no internet connection."""
    # Arrange
    mock_internet.return_value = False
    mock_valid.return_value = True

    # Act
    result = can_access_google_page("https://google.com")

    # Assert
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url(
    mock_valid: MagicMock, mock_internet: MagicMock
) -> None:
    """Test scenario: Internet is available but URL is invalid."""
    # Arrange
    mock_internet.return_value = True
    mock_valid.return_value = False

    # Act
    result = can_access_google_page("https://google.com")

    # Assert
    assert result == "Not accessible"
