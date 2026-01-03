from playwright.sync_api import Playwright


def test_api1(playwright:Playwright):
    request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
    response = request.post(url='/api/ecom/auth/login',
                 headers={'Content-Type':'application/json'},
                 data={"userEmail": "prakhar.sh95@gmail.com", "userPassword": "Password@123"})
    response_json = response.json()

def test_view_order(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("textbox", name="email@example.com").fill("prakhar.sh95@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").fill("Password@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    page.get_by_role("button", name="Sign Out").click()

    context.close()
    browser.close()

