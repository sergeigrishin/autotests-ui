from idlelib.pyshell import idle_showwarning
from tokenize import blank_re
from _pytest.fixtures import SubRequest
import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.parametrize('number', [1, 2, -1, 0])
def test_number(number: int):
    assert number > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Jo'])
class TestOperations:

    @pytest.mark.parametrize('account', ['Credit', 'Debet'])
    def test_user_with_operations(self, user: str, account: str):
        ...

    def test_user_without_operations(self, user):
        ...


users = {
    '911': 'user with money on bank account',
    '01': 'user without money on bank account',
    '88002000600': 'user operations on bank account'
}

@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number):
    ...
