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