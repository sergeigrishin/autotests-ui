import allure

@allure.step('Open browser')
def open_browser():
    ...

@allure.step('Creating course')
def create_course():
    ...

@allure.step('Closing browser')
def closing_browser():
    ...


def test_feature():
    open_browser()
    create_course()
    closing_browser()