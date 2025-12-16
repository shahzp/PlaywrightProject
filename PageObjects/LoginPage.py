from playwright.sync_api import Page

from PageObjects.DashboardPage import DashboardPage


class LoginPage:
    def __init__(self,page:Page):
        self.page = page

    def navigate(self,url):
        self.page.goto(url)

    def login(self,username,password):
        self.page.locator('#userEmail').fill(username)
        self.page.locator('#userPassword').fill(password)
        self.page.get_by_role('button', name='Login').click()
        dashboard_page=DashboardPage(self.page)
        return dashboard_page

