from playwright.sync_api import expect


class OrderDetailPage:
    def __init__(self, page):
        self.page = page

    def validateLabel(self):
        expect(self.page.get_by_text('Thank you for Shopping With Us')).to_be_visible()
