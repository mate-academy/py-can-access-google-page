import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,result",
    [
        ("Not google url", "Not accessible"),
        ("Some google url", "Accessible"),
        ("Not google url", "Not accessible"),
        ("Some google url", "Accessible")
    ]
)
def test_should_return_accessible_when_conditions_true(url: str,
                                                       result: str) -> None:
    with (mock.patch("app.main.valid_google_url",
                     lambda *args: True
                     if url == "Some google url"
                     else False),
            mock.patch("app.main.has_internet_connection", lambda: True)):
        assert can_access_google_page(url) == result


@pytest.mark.parametrize(
    "url,result",
    [
        ("Not google url", "Not accessible"),
        ("Some google url", "Not accessible"),
        ("Not google url", "Not accessible"),
        ("Some google url", "Not accessible")
    ]
)
def test_should_return_not_accessible_when_no_internet(url: str,
                                                       result: str) -> None:
    with (mock.patch("app.main.valid_google_url",
                     lambda *args: True
                     if url == "Some google url"
                     else False),
            mock.patch("app.main.has_internet_connection", lambda: False)):
        assert can_access_google_page(url) == result
