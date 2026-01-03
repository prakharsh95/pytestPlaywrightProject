from playwright.sync_api import Page, expect

from .logoutPage import logoutPage


class orderDetails:
    def __init__(self,page):
        self.page = page

    def view_order_details(self, order_id):
        order_ID_locator = self.page.locator("//div[@class='col-text -main']")
        expect(order_ID_locator).to_have_text(order_id)
        return logoutPage(self.page)
