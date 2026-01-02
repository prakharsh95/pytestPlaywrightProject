class API_Utils():
    def __init__(self, playwright):
        self.playwright = playwright
        self.context = self.playwright.request.new_context(base_url="https://rahulshettyacademy.com")

    def login(self):
        response = self.context.post(url='/api/ecom/auth/login',
                                     headers={'Content-Type': 'application/json'},
                                     data={"userEmail": "prakhar.sh95@gmail.com", "userPassword": "Password@123"})
        response_json = response.json()

        return response_json['token'], response_json['userId']



