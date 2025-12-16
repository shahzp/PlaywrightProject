import pytest
from playwright.sync_api import Playwright, expect
from Utilities.ReadJson import Jsonread

from Utilities.API_Base_Framework import API_util
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage

js=Jsonread()
dataList=js.readJson('Data/Credentials.json')

@pytest.mark.smoke
@pytest.mark.parametrize('login_creds',dataList)
def test_web_api(playwright:Playwright, login_creds,browser_instance):
    email=login_creds['email']
    password=login_creds['password']
    #Place order via API
    api=API_util()
    if api.getOrderId(playwright,email,password):
        order_id =api.getOrderId(playwright,email,password)
        print(f'order id is : {order_id}')
    else:
        print(f'Order is Not placed.')
        return

    loginPage=LoginPage(browser_instance)
    loginPage.navigate(url='https://rahulshettyacademy.com/client/')
    # page.goto('https://rahulshettyacademy.com/client/')
    dashboard_page=loginPage.login(email,password)

    #Got to orders and check order is created
    #page.get_by_role('button',name='  ORDERS').click()
    order_history_page=dashboard_page.clickOnOrders()
    order_detail_page=order_history_page.viewOrder(order_id)

    order_detail_page.validateLabel()

    #table=page.locator('.table')

    # Locate the order row by text (robust way)
    #Expecting only one row with this order id
    # order_row = table.locator("tbody tr", has_text=order_id)
    # print(order_row.text_content())
    # expect(order_row).to_be_visible()
    # order_row.get_by_role('button',name='View').click()
    # expect(page.get_by_text('Thank you for Shopping With Us')).to_be_visible()


