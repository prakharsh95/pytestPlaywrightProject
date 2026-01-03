class logoutPage:
    def __init__(self, page):
        self.page = page

    def logout(self):
        self.page.get_by_role("button", name="Sign Out").click()