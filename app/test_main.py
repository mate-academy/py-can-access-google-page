from unittest.mock import patch

import app.main as main_module


def test_can_access_google_page_accessible() -> None:
    with patch.object(main_module, "valid_google_url", return_value=True), \
         patch.object(main_module, "has_internet_connection",
                      return_value=True):

        result = main_module.can_access_google_page("https://www.google.com")

        assert result == "Accessible"


def test_can_access_google_page_invalid_url() -> None:
    with patch.object(main_module, "valid_google_url", return_value=False), \
         patch.object(main_module, "has_internet_connection",
                      return_value=True):

        result = main_module.can_access_google_page("https://not-google.com")

        assert result == "Not accessible"


def test_can_access_google_page_no_internet() -> None:
    with patch.object(main_module, "valid_google_url", return_value=True), \
         patch.object(main_module, "has_internet_connection",
                      return_value=False):

        result = main_module.can_access_google_page("https://www.google.com")

        assert result == "Not accessible"
