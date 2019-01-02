from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def returne_to_grups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.returne_to_grups_page()


    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_xpath("//body").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def created_contact(self, new_contact_group):
        wd = self.wd
        self.open_created_new_contact()
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
        wd.find_element_by_xpath("//div[@id='content']/form/select/option[13]").click()
        # Month Birthday
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]/option[7]").click()
        # Year Birthday
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(new_contact_group.byear)
        # Submint new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def created_2contact(self, new_contact_group):
        wd = self.wd
        self.open_created_new_contact()
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
        wd.find_element_by_xpath("//div[@id='content']/form/select/option[15]").click()
        # Month Birthday
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]/option[9]").click()
        # Year Birthday
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(new_contact_group.byear)
        # Submint new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def open_created_new_contact(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def destroy (self):
        self.wd.quit()