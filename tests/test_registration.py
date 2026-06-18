import pytest
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    'email, username, password',
    [('user@gmail.com', 'username', 'password')]
)
def test_successful_registration(dashboard_page: DashboardPage, registration_page:RegistrationPage, email:str, username:str, password:str):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()

    dashboard_page.visible_title_text()
