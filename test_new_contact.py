# -*- coding: utf-8 -*-
import unittest
from new_contact_group import New_contact_group
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class TestNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, password="secret", username="admin")
        self.open_created_new_contact(wd)
        self.created_contact(wd, New_contact_group(firstname = "Мышин", middlename = "Виссарионий",
                                                   lastname= "Альбертович", address = "Болотная улица",
                                                   homephone = "89589765421", mobile = "89458966525",
                                                   email = "bred@yandex.ru",
                                                   bday = "9", bmonth = "May", byear = "1987"))
        self.return_home_page(wd)
        self.logout(wd)

    def test_new_2_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, password="secret", username="admin")
        self.open_created_new_contact(wd)
        self.created_contact(wd, New_contact_group(firstname = "Хрящин", middlename = "Петро",
                                                   lastname= "Васильевич", address = "Парнокопытная улица",
                                                   homephone = "89589762698", mobile = "89458966684",
                                                   email = "хрунов@yandex.ru",
                                                   bday = "9", bmonth = "May", byear = "1993"))
        self.return_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def created_contact(self, wd, new_contact_group):
        # Created new contact
        # Firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(new_contact_group.firstname)
        # Middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(new_contact_group.middlename)
        # Lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(new_contact_group.lastname)
        # Address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(new_contact_group.address)
        # Home phone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(new_contact_group.homephone)
        # Mobile phone
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(new_contact_group.mobile)
        # E-mail
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(new_contact_group.email)
        # Date Birthday
        # Day Birthday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(new_contact_group.bday)
        wd.find_element_by_xpath("//div[@id='content']/form/select/option[11]").click()
        # Month Birthday
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(new_contact_group.bmonth)
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]/option[6]").click()
        # Year Birthday
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(new_contact_group.byear)
        # Submint new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_created_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, password, username):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
