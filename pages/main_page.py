from .base_page import BasePage

class MainPage(BasePage):
	def go_to_login_page(self):
		login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
		login_link.click() 