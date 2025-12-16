import time

from playwright.sync_api import Page


def test_launchBrowser(page: Page):
    page.goto("https://rahulshettyacademy.com")
    time.sleep(5)

def test_basicLocators(page:Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('learning')
    page.get_by_role('radio',name='User').check()
    page.get_by_role('combobox').select_option('teach')
    page.locator('#terms').check()
    #page.get_by_role('button',name='Sign In').click()

    time.sleep(5)
