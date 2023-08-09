from app.main import can_access_google_page
import pytest
from unittest import mock

#1 - проверить временной променжуток с 6.00 по 23.00
#2 - проверить работоспособность сайта
#3 - проверить временной променжуток
#4 - проверить тип возвращаемых данных
#5 - проверить что возвращает на неправильный тип данных (не строка ине путь)


class CanAccessGooglePage:
    def test_cannot_access_if_connection_or_valid_url_is_true(self) -> None:
        pass

    def test_cannot_access_if_only_connection(self) -> None:
        pass

    def test_cannot_access_if_only_valid_url(self) -> None:
        pass

