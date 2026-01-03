from .ordersPage import ordersPage


class dashboard:
    def __init__(self, page):
        self.page = page

    def go_to_orders(self):
        self.page.get_by_role("button", name="ORDERS").click()
        return ordersPage(self.page)