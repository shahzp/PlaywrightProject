import json

from playwright.sync_api import Page, expect,Playwright

from Utilities.API_Base import API_util


def test_mock_response(page:Page):

    page.goto('https://rahulshettyacademy.com/client/')
    mocked_rsponse = {"data": [], "message": "No Orders"}

    # Create handler before action
    def handler(route):
        route.fulfill(status=200, json=mocked_rsponse)

    # Create Route
    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*', handler)
    page.locator('#userEmail').fill('sastrypokkuluri@gmail.com')
    page.locator('#userPassword').fill('Infy@123')
    page.get_by_role('button', name='Login').click()



    #click on orders action
    page.get_by_role('button', name='  ORDERS').click()
    ui_message=page.locator('.mt-4').text_content()
    print(ui_message)
    expect(page.locator('.mt-4')).to_contain_text('Please Visit')
    page.unroute('https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*')

def test_mock_Request(page:Page):
    page.goto('https://rahulshettyacademy.com/client/')
    #mock url with order id of some other account
    mocked_request_url ='https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=693dcff032ed86587131d464'

    # Create handler before action
    def handler(route,request):
        mycopy=request.copy()
        mycopy.url=''
        route.continue_(url=mocked_request_url)

    # Create Route using glob pattern
    page.route('**/get-orders-details?*', handler)
    page.locator('#userEmail').fill('sastrypokkuluri@gmail.com')
    page.locator('#userPassword').fill('Infy@123')
    page.get_by_role('button', name='Login').click()
    page.get_by_role('button', name='  ORDERS').click()
    table = page.locator('.table')
    order_row = table.locator("tbody tr", has_text='693da9e832ed86587131a76f')
    #expect(order_row).to_be_visible()
    order_row.get_by_role('button', name='View').click()
    message=page.get_by_text('You are not authorize to view this order')
    print(message.text_content())
    expect(message).to_be_visible()
    page.unroute('**/get-orders-details?*')

def test_session_storage(playwright:Playwright):
    api=API_util()
    #Get token via API. So will always get latest token and no expiry issue
    token=api.getToken(playwright)
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    #Add at context level
    context.add_init_script(f'''localStorage.setItem('token','{token}') ''')

    page = context.new_page()
    page.goto('https://rahulshettyacademy.com/client/')
    # save state after navigation
    context.storage_state(path='auth.json')
    page.get_by_role('button',name='ORDERS').click()
    expect(page.get_by_text('Your Orders')).to_be_visible()
    import os
    with open('auth.json') as f:
        auth = json.load(f)
        mydict=auth['origins'][0]['localStorage'][0]
        for k,v in mydict.items():
            if v=='token':
                print(f'token is {mydict["value"]}')
                break