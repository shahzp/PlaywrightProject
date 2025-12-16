from playwright.sync_api import Page, expect


def test_uiChecks(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_visible()
    page.locator('#hide-textbox').click()
    expect(page.get_by_placeholder('Hide/Show Example')).not_to_be_visible()

    page.once("dialog", lambda d: d.accept())
    page.get_by_role("button", name="Confirm").click()

    # with page.expect_event('dialog') as dialog_info:
    #     page.get_by_role('button', name='Confirm').click()
    # dialog=dialog_info.value
    # dialog.accept()

    myFrame=page.frame_locator('#courses-iframe')
    myFrame.get_by_role('link',name='All-Access').first.click()
    expect(myFrame.locator('body')).to_contain_text('one Single Subscription')

def test_webTables(page:Page):
    page.goto('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    table=page.locator('table')
    rice_price=None
    #row = table.get_by_role('row', name='Rice')
    row=table.locator('tr:has(td:text("Rice"))')
    for i in range(table.locator('th').count()):
        if table.locator('th').nth(i).text_content()=='Price':
            rice_price=int(row.locator('td').nth(i).text_content())
            break
    assert rice_price==37
