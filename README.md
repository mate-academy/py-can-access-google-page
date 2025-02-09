# Can access Google page

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Inside `app/test_main.py`, write a test for `can_access_google_page` function. This function takes
`url` of the site, returns `"Accessible"` if `url` is valid to 
access the Google home page and 
it has internet connection, else it returns `"Not accessible"`.

This function uses:
- `valid_google_url` function, that takes `url` and return `True` if
`url` is in valid values.
- `has_internet_connection` function, returns `True` if current time is
between 6:00:00 and 22:59:59, because internet connection exists
only in this period of time in this town.

You have to check only `can_access_google_page` functionality. Mock 
`valid_google_url` and `has_internet_connection` functions.

You have to install `requests` via pip.

Run `pytest app/` to check if function pass your tests. 

Run `pytest --numprocesses=auto tests/` to check if your tests cover all boundary conditions and pass task tests.




Усередині `app/test_main.py` напишіть тест для функції `can_access_google_page`. Ця функція приймає
`url` сайту, повертає `"Доступний", якщо `url` дійсний для
отримати доступ до домашньої сторінки Google і
він має підключення до Інтернету, інакше він повертає `"Недоступний"`.

Ця функція використовує:
- функція `valid_google_url`, яка приймає `url` і повертає `True`, якщо
`url` має дійсні значення.
- функція `has_internet_connection`, повертає `True`, якщо поточний час є
з 6:00:00 до 22:59:59, оскільки доступ до Інтернету є
тільки в цей період часу в цьому місті.

Ви повинні перевірити лише функціональність `can_access_google_page`. макет
Функції `valid_google_url` і `has_internet_connection`.

Ви повинні встановити `requests` через pip.

Запустіть `pytest app/`, щоб перевірити, чи функція пройшла ваші тести.

Запустіть `pytest --numprocesses=auto tests/`, щоб перевірити, чи ваші тести охоплюють усі граничні умови та проходять тести завдань.
