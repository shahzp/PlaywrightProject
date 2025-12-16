from playwright.sync_api import expect

from PageObjects.OrderDetailPage import OrderDetailPage


class OrderHistoryPage:
    def __init__(self,page):
        self.page=page

    def viewOrder(self,order_id):
        table = self.page.locator('.table')
        order_row = table.locator("tbody tr", has_text=order_id)
        #print(order_row.text_content())
        expect(order_row).to_be_visible()
        order_row.get_by_role('button', name='View').click()
        order_detail_page=OrderDetailPage(self.page)
        return  order_detail_page
