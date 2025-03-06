from unittest import TestCase, mock


from app.main import can_access_google_page


class TestGeneral(TestCase):
    def test_func_use_all_needed_func(self) -> None:
        with mock.patch(
                "app.main.valid_google_url",
                return_value=True
        ) as mocked_valid:
            with mock.patch(
                    "app.main.has_internet_connection",
                    return_value=True
            ) as mocked_has_internet:
                can_access_google_page("http:bos")
                mocked_valid.assert_called_once_with("http:bos")
                mocked_has_internet.assert_called_once()
