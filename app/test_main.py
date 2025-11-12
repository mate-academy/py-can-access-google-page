from typing import Any
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page(mock_1: Any, mock_2: Any) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


def test_cant_access_wrong_page() -> None:
    with (mock.patch("app.main.valid_google_url") as m_valid,
          mock.patch("app.main.has_internet_connection") as m_net):
        m_valid.return_value = False
        m_net.return_value = True
        assert can_access_google_page("hts://gogle.com") == "Not accessible"


def test_cannot_access_page_w_o_internet() -> None:
    with (mock.patch("app.main.valid_google_url") as m_valid,
          mock.patch("app.main.has_internet_connection") as m_net):
        m_valid.return_value = True
        m_net.return_value = False
        assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_cant_access_wrong_page_without_internet(
        mock_1: Any, mock_2: Any
) -> None:
    assert can_access_google_page("htp://ggle.cosn") == "Not accessible"
