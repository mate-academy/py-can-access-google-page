import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,"
    "connection,"
    "expected_result",
    [
        pytest.param(
            True, True, "Accessible",
            id="should be 'Accessible' with valid url and internet connection"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="should be 'Not accessible' with incorrect url"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="should be 'Not accessible' w/o internet connection"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="should be 'Not accessible' with incorrect url and w/o internet"
        ),
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        connection: bool,
        expected_result: str
) -> None:
    with (mock.patch("app.main.valid_google_url",
                     return_value=valid_url),
          mock.patch("app.main.has_internet_connection",
                     return_value=connection)):
        assert can_access_google_page("") == expected_result
