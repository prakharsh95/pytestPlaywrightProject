

class API_Utils():
    def __init__(self, playwright):
        self.playwright = playwright
        self.context = self.playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        self.token = None
        self.user_id = None

    def login(self):
        response = self.context.post(url='/api/ecom/auth/login',
                                     headers={'Content-Type': 'application/json'},
                                     data={"userEmail": "prakhar.sh95@gmail.com", "userPassword": "Password@123"})
        response_json = response.json()
        
        self.token = response_json['token']
        self.user_id = response_json['userId']
        
        return self.token, self.user_id

    def create_order(self):
        # Automatically login if token is not set
        if self.token is None:
            self.login()
        
        headers = {'Content-Type': 'application/json',
                   'Authorization': self.token}
        payload = {"orders":[{"country":"India",
                              "productOrderedId":"68a961459320a140fe1ca57a"}]}

        response = self.context.post(url='/api/ecom/order/create-order',
                                     data=payload,
                                     headers=headers)
        response_json = response.json()
        assert response_json['message']
        return response_json['orders'][0]

    def delete_order(self, order_id):
        # Automatically login if token is not set
        if self.token is None:
            self.login()
        
        headers = {'Content-Type': 'application/json',
                   'Authorization': self.token}
        response = self.context.delete(url=f'/api/ecom/order/delete-order/{order_id}',
                                       headers=headers)
        assert response.status == 200, f"Expected status code 200, but got {response.status}"
        response_json = response.json()
        assert response_json['message'] == "Orders Deleted Successfully", f"Expected message 'Orders Deleted Successfully', but got '{response_json.get('message', 'No message field')}'"




