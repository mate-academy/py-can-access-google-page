from app import main


def test_accessible_if_hic_and_vgu(monkeypatch) -> None:  # noqa: ANN001
    def mock_h_i_c() -> bool:
        return True

    def mock_v_g_u(url: str) -> bool:
        return True

    monkeypatch.setattr(main, "valid_google_url", mock_v_g_u)
    monkeypatch.setattr(main, "has_internet_connection", mock_h_i_c)
    assert main.can_access_google_page("zdfbzdf") == "Accessible"


def test_accessible_if_only_hic(monkeypatch) -> None:  # noqa: ANN001
    def mock_h_i_c() -> bool:
        return True

    def mock_v_g_u(url: str) -> bool:
        return False

    monkeypatch.setattr(main, "valid_google_url", mock_v_g_u)
    monkeypatch.setattr(main, "has_internet_connection", mock_h_i_c)
    assert main.can_access_google_page("zdfbzdf") == "Not accessible"


def test_accessible_if_only_vgu(monkeypatch) -> None:  # noqa: ANN001
    def mock_h_i_c() -> bool:
        return False

    def mock_v_g_u(url: str) -> bool:
        return True

    monkeypatch.setattr(main, "valid_google_url", mock_v_g_u)
    monkeypatch.setattr(main, "has_internet_connection", mock_h_i_c)
    assert main.can_access_google_page("zdfbzdf") == "Not accessible"
