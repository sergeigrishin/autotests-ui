from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=Settings.headless)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_locator = page.get_by_test_id('login-form-email-input').locator('input')
    email_locator.focus()

    for char in "user@mail.ru":
        page.keyboard.type(char)

    page.keyboard.press("ControlOrMeta+A")


    page.wait_for_timeout(5000)
