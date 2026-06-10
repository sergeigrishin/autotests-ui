import pytest

@pytest.fixture(autouse=True) #Фикстура запускается автоматически до теста
def send_analytics_data():
    print("[AUTOUSE] Отправляем дынные в сервис аналитики")

@pytest.fixture(scope='session') #Фикстура на определенное покрытие
def setting():
    print('[SESSION] Инициализируем настройки автотестов')

@pytest.fixture(scope='class')
def user():
    print('[CLASS] Создаем данные пользователя один раз на тестовый класс')

@pytest.fixture(scope='function')
def browser():
    print("[FUNCTION] Открываем браузер на каждый тест")


class TestUserFlow:
    def test_user_can_login(self, setting, user, browser):
        ...

    def test_user_can_create_course(self, setting, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, setting, user, browser):
        ...




