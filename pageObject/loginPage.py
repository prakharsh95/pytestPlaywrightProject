from .dashboard import dashboard


class loginPage:
    def __init__(self, page):
        self.page = page

    def login(self, user_name, password):
        self.page.get_by_role("textbox", name="email@example.com").fill(user_name)
        self.page.get_by_role("textbox", name="enter your passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        return dashboard(self.page)
