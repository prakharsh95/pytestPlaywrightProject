from .orderDetails import orderDetails


class ordersPage:
    def __init__(self, page):
        self.page = page

    def view_order(self, order_id):
        order_row_locator = self.page.locator('//tr').filter(has_text=order_id)
        order_row_locator.locator('//button').filter(has_text='View').click()
        return orderDetails(self.page)