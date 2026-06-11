import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        print('ДО')
        yield browser.new_page()
        print('ПОСЛЕ')



