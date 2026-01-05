import pytest
from pytest_bdd import scenario, given, when, then, parsers
from playwright.sync_api import Playwright

from pageObject.loginPage import loginPage
from utils.API_utils import API_Utils

# Shared state to store order_id between steps
@pytest.fixture(scope="function")
def order_context():
    """Fixture to store shared state between steps"""
    return {}


@given(parsers.parse('I create an order via API with "{userName}" and "{password}"'))
def create_order_via_api(playwright: Playwright, userName, password, order_context):
    """Step to create an order via API"""
    api_utils = API_Utils(playwright)
    order_id = api_utils.create_order(userName, password)
    order_context['order_id'] = order_id
    order_context['api_utils'] = api_utils
    order_context['userName'] = userName
    order_context['password'] = password


@when(parsers.parse('I login to the application with "{userName}" and "{password}"'))
def login_to_application(setup_browser, userName, password, order_context):
    """Step to login to the application"""
    page = setup_browser
    page.goto("https://rahulshettyacademy.com/client")
    login_page = loginPage(page)
    dashboard = login_page.login(userName, password)
    order_context['page'] = page
    order_context['dashboard'] = dashboard


@when('I navigate to the orders page')
def navigate_to_orders_page(order_context):
    """Step to navigate to orders page"""
    dashboard = order_context['dashboard']
    orders_page = dashboard.go_to_orders()
    order_context['orders_page'] = orders_page


@when('I view the order with order ID')
def view_order_with_id(order_context):
    """Step to view the order"""
    orders_page = order_context['orders_page']
    order_id = order_context['order_id']
    order_details_page = orders_page.view_order(order_id)
    order_context['order_details_page'] = order_details_page


@then('I should see the order details matching the order ID')
def verify_order_details(order_context):
    """Step to verify order details"""
    order_details_page = order_context['order_details_page']
    order_id = order_context['order_id']
    logout = order_details_page.view_order_details(order_id)
    order_context['logout'] = logout


@then('I delete the order via API')
def delete_order_via_api(order_context):
    """Step to delete the order via API"""
    api_utils = order_context['api_utils']
    order_id = order_context['order_id']
    userName = order_context['userName']
    password = order_context['password']
    api_utils.delete_order(order_id, userName, password)


@then('I logout from the application')
def logout_from_application(order_context):
    """Step to logout from the application"""
    logout = order_context['logout']
    logout.logout()


# Load the feature file and create test function
@scenario("feature/orderTransaction.feature", "View order details after creating an order")
def test_view_order_bdd():
    """BDD test for viewing order details"""
    pass
