import pytest
from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.fixture()
    def mocked_valid_google_url(self) -> bool:
        with mock.patch("app.main.valid_google_url") as mocked_url:
            yield mocked_url

    @pytest.fixture()
    def mocked_has_internet_connection(self) -> bool:
        with mock.patch("app.main.has_internet_connection")\
                as mocked_connection:
            yield mocked_connection

    @pytest.mark.parametrize(
        "url,connection,access",
        [
            pytest.param(True, True, "Accessible",
                         id="If both are True should Accessible"),
            pytest.param(True, False, "Not accessible",
                         id="If one is False should Not accessible"),
            pytest.param(False, True, "Not accessible",
                         id="If one is False should Not accessible"),
            pytest.param(False, False, "Not accessible",
                         id="If both are False should Not accessible")
        ]
    )
    def test_can_access_google_page(
            self,
            mocked_valid_google_url: bool,
            mocked_has_internet_connection: bool,
            url: bool,
            connection: bool,
            access: str
    ) -> None:
        mocked_valid_google_url.return_value = url
        mocked_has_internet_connection.return_value = connection
        assert can_access_google_page("http://url") == access


if __name__ == "__main__":
    pytest.main()
