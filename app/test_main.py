from unittest import mock
import datetime

from app.main import can_access_google_page, has_internet_connection


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


def test_has_internet_connection_at_6() -> None:
    boundary_time = datetime.datetime(2026, 9, 22, 6, 0, 0)
    with mock.patch(
        "app.main.datetime.datetime"
    ) as datetime_mock:
        datetime_mock.now.return_value = boundary_time
        assert has_internet_connection() is True


def test_has_internet_connection_at_5_59() -> None:
    boundary_time = datetime.datetime(2026, 9, 22, 5, 59, 0)
    with mock.patch(
        "app.main.datetime.datetime"
    ) as datetime_mock:
        datetime_mock.now.return_value = boundary_time
        assert has_internet_connection() is False


def test_has_internet_connection_at_22_59() -> None:
    boundary_time = datetime.datetime(2026, 9, 22, 22, 59, 59)
    with mock.patch(
        "app.main.datetime.datetime"
    ) as datetime_mock:
        datetime_mock.now.return_value = boundary_time
        assert has_internet_connection() is True


def test_has_internet_connection_at_23_00() -> None:
    boundary_time = datetime.datetime(2026, 9, 22, 23, 0, 0)
    with mock.patch(
        "app.main.datetime.datetime"
    ) as datetime_mock:
        datetime_mock.now.return_value = boundary_time
        assert has_internet_connection() is False


def test_has_internet_connection_at_13_12() -> None:
    boundary_time = datetime.datetime(2026, 9, 22, 13, 12, 0)
    with mock.patch(
        "app.main.datetime.datetime"
    ) as datetime_mock:
        datetime_mock.now.return_value = boundary_time
        assert has_internet_connection() is True


def test_has_internet_connection_at_03_40() -> None:
    boundary_time = datetime.datetime(2026, 9, 22, 3, 40, 0)
    with mock.patch(
        "app.main.datetime.datetime"
    ) as datetime_mock:
        datetime_mock.now.return_value = boundary_time
        assert has_internet_connection() is False
