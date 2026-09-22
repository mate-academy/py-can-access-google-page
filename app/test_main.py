from unittest import mock

from app.main import can_access_google_page


def test_should_return_accessible_if_valid_url_and_has_internet() -> None:
    with (
        mock.patch(
            "app.main.valid_google_url",
            return_value=True
        ),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=True
        )
    ):
        assert can_access_google_page(
            "https://www.google.com"
        ) == "Accessible"


def test_should_return_not_accessible_if_valid_url_is_false() -> None:
    with (
        mock.patch(
            "app.main.valid_google_url",
            return_value=False
        ),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=True
        )
    ):
        assert can_access_google_page(
            "https://www.google.com"
        ) == "Not accessible"


def test_should_return_not_accessible_if_has_no_internet() -> None:
    with (
        mock.patch(
            "app.main.valid_google_url",
            return_value=True
        ),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=False
        )
    ):
        assert can_access_google_page(
            "https://www.google.com"
        ) == "Not accessible"


def test_should_return_not_accessible_if_both_functions_are_false() -> None:
    with (
        mock.patch(
            "app.main.valid_google_url",
            return_value=False
        ),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=False
        )
    ):
        assert can_access_google_page(
            "https://www.google.com"
        ) == "Not accessible"


def test_should_not_call_valid_url_if_has_no_internet() -> None:
    with (
        mock.patch(
            "app.main.valid_google_url",
            return_value=True
        ) as valid_url_mock,
        mock.patch(
            "app.main.has_internet_connection",
            return_value=False
        )
    ):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"
        valid_url_mock.assert_not_called()
