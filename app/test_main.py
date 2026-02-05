@pytest.mark.parametrize(
    "internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_scenarios(
    internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    url = "https://www.google.com"

    with patch(
        "app.main.has_internet_connection",
        return_value=internet,
    ), patch(
        "app.main.valid_google_url",
        return_value=valid_url,
    ):
        assert can_access_google_page(url) == expected
