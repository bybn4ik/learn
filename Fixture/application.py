from selenium.webdriver.firefox.webdriver import WebDriver

from Fixture.group import GroupHelper
from Fixture.session import SessionHelper
from Fixture.new_contact_group import New_contact_groupHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.new_contact_group = New_contact_groupHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy (self):
        self.wd.quit()