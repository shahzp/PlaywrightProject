from playwright.sync_api import Playwright,Page

from PageObjects.OrderHistoryPage import OrderHistoryPage


class DashboardPage:
    def __init__(self,page:Page):
        self.page = page

    def clickOnOrders(self)->OrderHistoryPage:
        self.page.get_by_role('button', name='  ORDERS').click()
        order_history_page=OrderHistoryPage(self.page)
        return  order_history_page