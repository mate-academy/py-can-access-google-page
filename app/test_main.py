from __future__ import annotations

from unittest import mock

import pytest

from app.main import can_access_google_page
from unittest.mock import MagicMock


class TestCanAccessPooglePage:
    @pytest.fixture()
    def mock_valid_google_url(self) -> MagicMock:
        with mock.patch("app.main.valid_google_url") as mock_function:
            yield mock_function

    @pytest.fixture()
    def mock_has_internet_connection(self) -> MagicMock:
        with mock.patch("app.main.has_internet_connection") as mock_function:
            yield mock_function

    def test_return_accessible_if_ok(
        self,
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
    ) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True

        assert (
            can_access_google_page("https.google.com") == "Accessible"
        ), "Should return Accessible if both funcs return ok"

    def test_both_funcs_called(
        self,
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
    ) -> None:
        can_access_google_page("https.google.com")

        mock_valid_google_url.assert_called()
        mock_has_internet_connection.assert_called()

    def test_valid_google_url_called_with_correct_url(
        self,
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
    ) -> None:
        can_access_google_page("https.google.com")

        mock_valid_google_url.assert_called_with("https.google.com")

    def test_return_not_accessible_if_false_valid_google_url(
        self,
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
    ) -> None:
        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True

        assert (
            can_access_google_page("https.google.com") == "Not accessible"
        ), "Should return Not accessible if valid_google_url is False"

    def test_return_not_accessible_if_has_internet_connection_false(
        self,
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
    ) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False

        assert (
            can_access_google_page("https.google.com") == "Not accessible"
        ), "Should return Not accessible if has_internet_connection is False"
