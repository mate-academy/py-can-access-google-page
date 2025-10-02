from unittest import mock
import pytest
from typing import Any
from app.main import can_access_google_page


def test_can_access_google_page_str() -> None:
    assert isinstance(can_access_google_page("https://www.google.com/"), str)


@pytest.mark.parametrize(
    "internet, url, expected",
    [
        pytest.param(True, False, "Not accessible",
                     id="(True, False)->Not accessible"),
        pytest.param(False, True, "Not accessible",
                     id="(False, True)->Not accessible"),
        pytest.param(True, True, "Accessible",
                     id="(True, True)->Accessible"),
    ]
)
def test_can_access_google_page_with_various_combinations(internet: bool,
                                                          url: bool,
                                                          expected: Any
                                                          ) -> None:
    with (mock.patch("app.main.has_internet_connection",
                     return_value=internet)):
        with mock.patch("app.main.valid_google_url", return_value=url):
            assert can_access_google_page("https://www.google.com/"
                                          ) == expected
