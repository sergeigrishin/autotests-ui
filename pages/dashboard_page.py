from pages.base_page import Basepage
from playwright.sync_api import sync_playwright, expect

class DashboardPage(Basepage):
    def __init__(self, page):
        super().__init__(page)

        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    def visible_title_text(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text('Dashboard')