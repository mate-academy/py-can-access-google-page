import pytest


from unittest import mock


from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, has_connection, expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Can access Google page"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="url is not valid"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="No internet connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Invalid url and no internet connection"
        ),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_functionality_can_access_google_page(
    mocked_url_func,
    mocked_connection_func,
    is_valid_url,
    has_connection,
    expected
):
    mocked_url_func.return_value = is_valid_url
    mocked_connection_func.return_value = has_connection

    assert can_access_google_page("google.com") == expected
