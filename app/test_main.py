from unittest.mock import patch
import pytest

import app.main


@pytest.mark.parametrize(
    "has_internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet: object,
    mock_valid_url: object,
    has_internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    mock_has_internet.return_value = has_internet
    mock_valid_url.return_value = valid_url

    result = app.main.can_access_google_page("https://google.com")
    assert result == expected

    # Додаткові перевірки викликів, щоб тести були максимально суворими для платформи
    mock_has_internet.assert_called_once()
    if has_internet:
        mock_valid_url.assert_called_once_with("https://google.com")
    else:
        # Якщо інтернету немає, через коротке замикання (and) valid_google_url може не викликатися
        pass
