from unittest.mock import MagicMock, patch

import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    (
        "is_url_valid",
        "has_connection",
        "expected_result",
        "url_to_test",
        "test_id",
    ),
    [
        (True, True, "Accessible", "https://valid.com",
         "URL Válida e Com Conexão"),
        (True, False, "Not accessible", "https://valid.com",
         "URL Válida e Sem Conexão"),
        (False, True, "Not accessible", "invalid-url",
         "URL Inválida e Com Conexão"),
        (False, False, "Not accessible", "invalid-url",
         "URL Inválida e Sem Conexão"),
    ],
    ids=lambda val: val if isinstance(val, str) else "",
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_scenarios(
    mock_valid_url: MagicMock,
    mock_has_connection: MagicMock,
    is_url_valid: bool,
    has_connection: bool,
    expected_result: str,
    url_to_test: str,
    test_id: str,
) -> None:
    mock_valid_url.return_value = is_url_valid
    mock_has_connection.return_value = has_connection

    result = can_access_google_page(url_to_test)

    assert result == expected_result
    mock_has_connection.assert_called_once()

    if has_connection:
        mock_valid_url.assert_called_once_with(url_to_test)
    else:
        mock_valid_url.assert_not_called()
