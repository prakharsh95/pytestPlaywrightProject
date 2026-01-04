import json
from pathlib import Path

import pytest
from playwright.sync_api import Playwright

from pageObject.loginPage import loginPage
from utils.API_utils import API_Utils

project_root = Path(__file__).parent
credentials_path = project_root / "data" / "credentials.json"

# Read userCredentials from credentials.json
with open(credentials_path, 'r') as f:
    credentials_data = json.load(f)
    user_credentials = credentials_data['userCredentials']



@pytest.mark.parametrize('user_credentials',user_credentials)
def test_view_order(playwright:Playwright,user_credentials, indirect=True):
    user_name = user_credentials['userEmail']
    password = user_credentials['userPassword']

    api_utils = API_Utils(playwright)
    order_id = api_utils.create_order()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    login_page = loginPage(page)
    dashboard = login_page.login(user_name, password)
    orders_page = dashboard.go_to_orders()
    order_details_page = orders_page.view_order(order_id)

    logout = order_details_page.view_order_details(order_id)
    api_utils.delete_order(order_id)
    logout.logout()



    context.close()
    browser.close()

