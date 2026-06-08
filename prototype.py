from playwright.sync_api import sync_playwright, expect, Request, Response

def log_request(request: Request):
    print(f'Request {request.url}, {request.method}')

def log_response(response: Response):
    print(f'Response {response.url}, {response.status}')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    page.on("request", log_request)
    page.on("response", log_response)

    button_registration = page.get_by_test_id("registration-page-registration-button")
    button_registration.is_disabled()

    email_locator = page.get_by_test_id("registration-form-email-input").locator('input')
    email_locator.focus()
    for char in "user.name@gmail.com":
        page.keyboard.type(char)

    user_locator = page.get_by_test_id("registration-form-username-input").locator("input")
    user_locator.fill("username")

    password_locator = page.get_by_test_id("registration-form-password-input").locator("input")
    password_locator.fill("username")

    button_registration.is_enabled()


