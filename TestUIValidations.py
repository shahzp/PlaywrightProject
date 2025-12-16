import time

from playwright.sync_api import Page, expect


def test_uiValdiation(page:Page):
    products=['iphone X','Nokia Edge']
    page.goto('https://rahulshettyacademy.com/angularpractice/shop')
    locator=page.locator('app-card')
    for product in products:
        filtered=locator.filter(has_text=product)
        if filtered :
            filtered.get_by_role('button',name='Add').click()

    page.get_by_text('Checkout').click()
    expect(page.locator('.media-body')).to_have_count(2)
    checkouts=page.locator('tr')
    finalProds=[]
    for product in products:
        filtered=locator.filter(has_text=product)
        finalProds.append(filtered)
    assert len(finalProds)==2

def test_childWindow(page:Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')

    with page.expect_popup() as popup:
        page.locator('.blinkingText').click()
    childPage=popup.value
    text=childPage.locator('.red').text_content()
    print(text)
    email=text.split(' ')[4].strip()
    assert email=='mentor@rahulshettyacademy.com'




