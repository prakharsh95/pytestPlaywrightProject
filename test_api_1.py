from playwright.sync_api import Playwright


def test_api1(playwright:Playwright):
    request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
    response = request.post(url='/api/ecom/auth/login',
                 headers={'Content-Type':'application/json'},
                 data={"userEmail": "prakhar.sh95@gmail.com", "userPassword": "Password@123"})
    response_json = response.json()
