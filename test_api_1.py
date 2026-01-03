from playwright.sync_api import Playwright

from pageObject.loginPage import loginPage
from utils.API_utils import API_Utils


def test_api1(playwright:Playwright):
    request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
    response = request.post(url='/api/ecom/auth/login',
                 headers={'Content-Type':'application/json'},
                 data={"userEmail": "prakhar.sh95@gmail.com", "userPassword": "Password@123"})
    response_json = response.json()

def test_view_order(playwright:Playwright):
    api_utils = API_Utils(playwright)
    order_id = api_utils.create_order()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    login_page = loginPage(page)
    dashboard = login_page.login("prakhar.sh95@gmail.com","Password@123")
    orders_page = dashboard.go_to_orders()
    order_details_page = orders_page.view_order(order_id)
    logout = order_details_page.view_order_details(order_id)
    logout.logout()



    context.close()
    browser.close()

