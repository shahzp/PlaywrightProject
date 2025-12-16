import json

from playwright.sync_api import Playwright,APIRequestContext


class API_util:
    orderCreationPayload = '{"orders": [{"country": "India", "productOrderedId": "68a961719320a140fe1ca57c"}]}'
    def __init__(self):
        pass

    def getToken(self,playwright:Playwright) -> str:
        api_request_context=playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response=api_request_context.post('/api/ecom/auth/login',
                                          data=json.dumps({"userEmail": "sastrypokkuluri@gmail.com", "userPassword": "Infy@123"}),
                                          headers={'Content-Type': 'application/json'})
        token=response.json().get('token')
        api_request_context.dispose()
        print(token)
        return token


    def getOrderId(self,playwright:Playwright) -> str:
        token=self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_request_context.post('/api/ecom/order/create-order',
                                            data=API_util.orderCreationPayload,
                                            headers={'authorization':token,
                                                     'content-type': 'application/json'})
        body=response.json()
        print(body)
        if response.ok:
            order_id = body.get('orders')[0]
        else:
            print(response.json()['message'])
            return None
        api_request_context.dispose()
        print(order_id)
        return order_id

